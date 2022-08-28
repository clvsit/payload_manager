<template>
    <div class="payload-list">

        <div class="payload-list-header">
            <h3 v-text="title"></h3>
        </div>

        <div class="payload-list-body">
            <input-comp v-on:search="search" :inputList="inputList"></input-comp>
            <div class="data-area">
                <table-comp v-on:handle="tableHandle" :table="table" ref="tableComp"></table-comp>
            </div>
        </div>
    </div>
</template>

<script>
import InputComp from "../components/input_comp/InputComp.vue";
import TableComp from '../components/container_comp/TableComp.vue';

export default {
    name: "List",
    components: {
        InputComp,
        TableComp
    },
    data() {
        return {
            info: {},
            title: "",
            table: {
                titleConf: [
                    { name: "ID", width: "30%" },
                    { name: "修改时间", width: "15%" },
                ],
                isOp: true,
                opConf: {
                    add: { show: true },
                    refresh: { show: true },
                    edit: { show: true },
                    delete: { show: true }
                },
                data: [
                    [
                        {name: "id", value: "1231231236"},
                        {name: "date", value: "2022-08-28"},
                    ]
                ],
                total: 0
            },
            show: {param: {}},
            inputList: [
                {
                    "title": "ID",
                    "type": "text",
                    "placeholder": "",
                    "name": "id"
                },
                {
                    "title": "修改日期",
                    "type": "dateRange",
                    "name": "date"
                }
            ],
            input: {
                page: {
                    limit: 10,
                    current: 1
                }
            }
        }
    },
    created() {
        let _this = this;

        this.title = this.$route.query.title;
        this.$nextTick(() => {
            _this.setHeight();
            _this.request("get_config");
        });
    },
    methods: {
        setHeight() {
            let height = document.documentElement.clientHeight;
            document.getElementById("app").style.height = (height - 1) + "px";
            $(".right-body").height(height - 101);
        },
        selectDataTitleKey(dataList) {
            const showTitle = this.info.show.title;

            for (let i = 0, len = dataList.length; i < len; i++) {
                if (dataList[i].key === showTitle) {
                    this.table.titleConf.push({
                        name: dataList[i].name,
                        width: "55%"
                    });
                    this.show.param = dataList[i];
                    break;
                }
            }
        },
        setTableData(dataList) {
            let tableDataList = [];

            for (let i = 0; i < dataList.length; i++) {
                let data = dataList[i];

                tableDataList.push([
                    { name: "id", value: data.id, hidden: false },
                    { name: "date", value: data.date, hidden: false },
                    { name: this.show.param.key, value: data[this.show.param.key], hidden: false }
                ])
            }
            return tableDataList;
        },
        request(type) {
            let _this = this;

            if (type === "get_config") {
                $.ajax({
                    method: "GET",
                    url: "http://localhost:6869/config/get",
                    data: {
                        title: this.title
                    },
                    success(resp) {
                        const detailDict = resp.data.detail;

                        if (resp.code === 1) {
                            _this.info = detailDict;
                            _this.selectDataTitleKey(detailDict.data);
                            _this.request("get_data_list");
                        }
                        
                    }
                })
            }
            else if (type === "get_data_list") {
                $.ajax({
                    method: "GET",
                    url: "http://localhost:6869/data/list",
                    data: {
                        table: this.info.table,
                        query: JSON.stringify(this.input.search),
                        offset: (this.input.page.current - 1) * this.input.page.limit,
                        limit: this.input.page.limit
                    },
                    success(resp) {
                        

                        if (resp.code === 1) {
                            _this.selectDataTitleKey(resp.data.list);
                        }
                        
                    }
                })
            }
        },
        search(paramDict) {
            this.input.search = paramDict;
            this.request("get_group_list");
        },
        tableHandle(data) {
            const method = data.method;

            if (method === "refresh") {
                this.request("get_version_list");
            }
            else if (method === "add") {
                window.open("#/detail?title=" + this.title);
            }
            else if (method === "table") {
                const type = data.type;

                this.data.version.select = { ...this.data.version.list[data.idx] };

                if (type === "edit") {
                    $("#modalVersionEdit").modal({
                        backdrop: "static"
                    });
                }
                else if (type === "del") {
                    $("#modalVersionDelete").modal({
                        backdrop: "static"
                    });
                }
            }
            else if (method === "skip") {
                this.input.page = data.page;
                this.request("get_version_list");
            }
            else if (method === "limit") {
                this.input.page.limit = data.page.limit;
                this.request("get_version_list");
            }
        }
    }
}
</script>

<style lang="scss" scoped>
.payload-list {

    .payload-list-header {
        padding: 0 10px 10px;
        border-bottom: 2px dashed rgba(0, 0, 0, 0.1);
    }

    .payload-list-body {
        margin-top: 20px;

        .data-area {
            margin-top: 20px;
            border-top: 1px solid rgba(0, 0, 0, 0.1);
        }
    }
}
</style>