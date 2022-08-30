<template>
    <div class="table-area">
        <!-- 表格头部：每页展示与表格级的操作 -->
        <div class="table-header">
            <div class="table-setting">
                <form class="form-inline">
                    <label class="control-label">每页展示：</label>
                    <select v-model="page.limit" class="form-control wd-100">
                        <option value="5">5</option>
                        <option value="10">10</option>
                        <option value="15">15</option>
                        <option value="20">20</option>
                        <option value="30">30</option>
                        <option value="50">50</option>
                    </select>
                </form>
            </div>
            <div class="table-operate">
                <div class="btn-group flex-row">
                    <div v-if="table.opConf.import.show" @click="handle('import', $event)" class="btn btn-default">
                        <i class="glyphicon glyphicon-open mr-5"></i>
                        <span>导入</span>
                    </div>
                    <div v-if="table.opConf.export.show" data-toggle="dropdown" class="btn btn-default">
                        <i class="glyphicon glyphicon-save mr-5"></i>
                        <span class="mr-5">导出</span>
                        <span class="caret"></span>
                    </div>
                    <ul class="dropdown-menu">
                        <li><a class="cursor-pointer" @click="handle('export', $event)" v-for="(eItem, eIdx) in table.opConf.export.typeList" :key="eIdx" v-text="eItem.name" :data-type="eItem.type"></a></li>
                    </ul>
                    <div v-if="table.opConf.add.show" @click="handle('add', $event)" class="btn btn-default">
                        <i class="glyphicon glyphicon-plus mr-5"></i>
                        <span>添加</span>
                    </div>
                    <div v-if="table.opConf.trash.show" @click="handle('trash', $event)" class="btn btn-default">
                        <i class="glyphicon glyphicon-trash mr-5"></i>
                        <span>删除</span>
                    </div>
                    <div v-if="table.opConf.refresh.show" @click="handle('refresh', $event)" class="btn btn-default">
                        <i class="glyphicon glyphicon-refresh mr-5"></i>
                        <span>刷新</span>
                    </div>
                </div>
            </div>
        </div>

        <!-- 表格主体 -->
        <div v-if="table.data.length" class="table mt-10">
            <div class="table-row">
                <div class="table-cell font-bold" v-for="(item, idx) in table.titleConf" :key="idx"
                    :style="{ 'width': item.width }">
                    <span class="mr-5" v-text="item.name"></span>
                    <span @click="handle('sort', $event)" v-if="item.sort" :data-column="item.column">
                        <i v-if="sort.info[item.column].status == 0" class="glyphicon glyphicon-sort"
                            data-type="normal"></i>
                        <i v-else-if="sort.info[item.column].status == 1" class="glyphicon glyphicon-chevron-down"
                            data-type="desc"></i>
                        <i v-else class="glyphicon glyphicon-chevron-up" data-type="asc"></i>
                    </span>
                </div>
                <div v-if="table.isOp" class="table-cell text-center font-bold" style="width: 15%;">相关操作</div>
            </div>
            <div class="table-row" v-for="(row, rIdx) in table.data" :key="rIdx">
                <div class="table-cell" v-for="(cell, cIdx) in row" :key="cIdx" v-html="cell.value"
                    :style="{ 'width': table.titleConf[cIdx].width }"></div>
                <div v-if="table.isOp" @click="handle('table', $event)" class="table-cell text-center" :data-idx="rIdx"
                    style="width: 15%;">
                    <i v-if="table.opConf.view.show" class="glyphicon glyphicon-eye-open mr-10" data-type="view" data-toggle="tooltip" data-placement="left" title="查看"></i>
                    <i v-if="table.opConf.edit.show" class="glyphicon glyphicon-edit mr-10" data-type="edit" data-toggle="tooltip" data-placement="left" title="编辑"></i>
                    <i v-if="table.opConf.start.show" class="glyphicon glyphicon-play mr-10" data-type="start"></i>
                    <i v-if="table.opConf.stop.show" class="glyphicon glyphicon-stop mr-10" data-type="stop"></i>
                    <i v-if="table.opConf.delete.show" class="glyphicon glyphicon-trash mr-10" data-type="del" data-toggle="tooltip" data-placement="left" title="删除"></i>
                    <i v-for="(customItem, customIdx) in table.opConf.custom" class="glyphicon mr-10" 
                        :key="customIdx" 
                        :class="customItem.icon" 
                        :data-type="customItem.type"
                        data-toggle="tooltip" data-placement="left" :title="customItem.title"></i>
                </div>
            </div>
        </div>
        <div v-else class="text-center">
            <img class="no-content" src="~@/assets/images/no-content.png" />
        </div>

        <!-- 表格底部：页码与跳页 -->
        <div class="table-footer">
            <div class="page-info-area">
                <b>当前页码/总页码：</b><span v-text="page.current"></span> / <span class="mr-20" v-text="page.total"></span>
                <b>总记录数：</b><span v-text="table.total"></span>
            </div>
            <nav aria-label="Page navigation">
                <ul class="pagination">
                    <li @click="handle('skipFirst')">
                        <a aria-label="Previous">
                            <i class="glyphicon glyphicon-step-backward"></i>
                        </a>
                    </li>
                    <li @click="handle('skipPrev')">
                        <a><i class="glyphicon glyphicon-chevron-left"></i></a>
                    </li>
                    <li><input v-model="page.current" type="number" min="1" class="form-control wd-100 text-center" />
                    </li>
                    <li @click="handle('skipNext')"><a><i class="glyphicon glyphicon-chevron-right"></i></a>
                    </li>
                    <li @click="handle('skipLast')">
                        <a aria-label="Next">
                            <i class="glyphicon glyphicon-step-forward"></i>
                        </a>
                    </li>
                </ul>
            </nav>
        </div>
    </div>
</template>

<script>
export default {
    name: "TableComp",
    props: ["table"],
    data() {
        return {
            page: {
                limit: 10,
                current: 1,
                total: 1
            },
            sort: {
                info: {}
            }
        }
    },
    created() {
        if (!this.table.opConf.export) {
            this.table.opConf.export = { show: false }
        }
        if (!this.table.opConf.import) {
            this.table.opConf.import = { show: false }
        }
        if (!this.table.opConf.add) {
            this.table.opConf.add = { show: false }
        }
        if (!this.table.opConf.trash) {
            this.table.opConf.trash = { show: false }
        }
        if (!this.table.opConf.refresh) {
            this.table.opConf.refresh = { show: false }
        }
        if (!this.table.opConf.view) {
            this.table.opConf.view = { show: false }
        }
        if (!this.table.opConf.edit) {
            this.table.opConf.edit = { show: false }
        }
        if (!this.table.opConf.delete) {
            this.table.opConf.delete = { show: false }
        }
        if (!this.table.opConf.start) {
            this.table.opConf.start = { show: false }
        }
        if (!this.table.opConf.stop) {
            this.table.opConf.stop = { show: false }
        }

        let sortInfoDict = {};

        for (let i = 0, len = this.table.titleConf.length; i < len; i++) {
            const item = this.table.titleConf[i];

            if (item.sort) {
                sortInfoDict[item.column] = {
                    "status": 0
                };
            }
        }
        this.sort.info = sortInfoDict;
        
        this.$nextTick(() => {
            $('[data-toggle="tooltip"]').tooltip();
        });
    },
    watch: {
        "table.total"() {
            this.page.total = Math.ceil(this.table.total / this.page.limit);
        },
        "table.data"() {
            $('[data-toggle="tooltip"]').tooltip();
        },
        "page.current"() {
            if (this.page.current > this.page.total) {
                this.page.current = this.page.total;
            }
            else if (this.page.current < 1) {
                this.page.current = 1;
            }
            this.$emit("handle", {
                "method": "skip",
                "page": {
                    "limit": this.page.limit,
                    "current": this.page.current
                }
            });
        },
        "page.limit"() {
            this.page.total = Math.ceil(this.table.total / this.page.limit);
            this.$emit("handle", {
                "method": "limit",
                "page": {
                    "limit": Number(this.page.limit)
                }
            });
        }
    },
    methods: {
        handle(type, event) {
            if (type === "refresh") {
                this.$emit("handle", { "method": "refresh" });
            }
            else if (type === "export") {
                const exportType = event.target.dataset.type;
                this.$emit("handle", { "method": "export", "type": exportType });
            }
            else if (type === "import") {
                this.$emit("handle", { "method": "import" });
            }
            else if (type === "add") {
                this.$emit("handle", { "method": "add" });
            }
            else if (type === "trash") {
                this.$emit("handle", { "method": "trash" });
            }
            else if (type === "sort") {
                const target = event.target;

                if (target.tagName === "I") {
                    let type = target.dataset.type,
                        column = target.parentNode.dataset.column;

                    if (type === "normal") {
                        this.sort.info[column].status = 1;
                        this.$emit("handle", { "method": "sort", "column": column, "type": "desc" });
                    }
                    else if (type === "desc") {
                        this.sort.info[column].status = 2;
                        this.$emit("handle", { "method": "sort", "column": column, "type": "asc" });
                    }
                    else if (type === "asc") {
                        this.sort.info[column].status = 0;
                        this.$emit("handle", { "method": "sort", "column": column, "type": "normal" });
                    }
                }
            }
            else if (type === "table") {
                const target = event.target;

                if (target.tagName === "I") {
                    let type = target.dataset.type;
                    let idx = Number(target.parentNode.dataset.idx);

                    this.$emit("handle", { "method": "table", "idx": idx, "type": type });
                }
            }
            else if (type === "skipFirst") {
                this.page.current = 1;
            }
            else if (type === "skipPrev") {
                this.page.current = this.page.current - 1 > 0 ? this.page.current - 1 : 1
            }
            else if (type === "skipNext") {
                this.page.current = this.page.current + 1 <= this.page.total ? this.page.current + 1 : this.page.total
            }
            else if (type === "skipLast") {
                this.page.current = this.page.total;
            }
        },
        setPageCurrent(number) {
            this.page.current = number;
        }
    }
}
</script>

<style lang="scss" scoped>
.table-area {

    .table-header {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        padding: 10px;
        border-radius: 10px;
        // background-color: #f5f5f5;
        border-bottom: 1px solid #e5e5e5;

        .table-setting {
            display: flex;
            flex-direction: row;
            justify-content: start;
        }
    }

    i {
        cursor: pointer;
    }

    .table {
        width: 100%;
        border-collapse: collapse;
        border-spacing: 0;
        // border: 1px solid #e5e5e5;
        // border-radius: 10px;
        background-color: #fff;
        margin-top: 10px;
        overflow: hidden;

        .table-row {
            display: flex;
            flex-direction: row;
            border-radius: 10px;
            // border: 1px solid rgba(0, 0, 0, 0.1);

            .table-cell {
                display: flex;
                flex-direction: row;
                align-items: center;
                padding: 10px;
                border-collapse: collapse;
                border-spacing: 0;
                border: 1px solid #e5e5e5;
            }
        }
    }

    .no-content {
        height: 320px;
        margin-bottom: 30px;
    }

    .table-footer {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        padding: 10px 10px 0;
        border-radius: 10px;
        // background-color: #f5f5f5;
        border-top: 1px solid #e5e5e5;

        .page-info-area {
            height: 40px;
            line-height: 40px;
        }

        .pagination {
            display: flex;
            flex-direction: row;
            justify-content: end;
            height: 40px;
            margin-top: 0;
        }
    }
}
</style>