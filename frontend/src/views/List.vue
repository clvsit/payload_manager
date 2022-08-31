<template>
    <div class="payload-list">

        <div class="payload-list-header">
            <h3 v-text="info.title"></h3>
        </div>

        <div class="payload-list-body">
            <input-comp v-on:search="search" :inputList="inputList"></input-comp>
            <div class="data-area">
                <table-comp v-if="data.status !== 0" v-on:handle="tableHandle" :table="table" ref="tableComp">
                </table-comp>
                <loading-comp v-else></loading-comp>
            </div>
        </div>

        <!-- 删除数据弹窗 -->
        <div id="modalDelete" class="modal fade" role="dialog">
            <div class="modal-dialog" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <h4 class="modal-title">删除数据</h4>
                    </div>
                    <div class="modal-body">
                        <div class="alert-message">
                            是否删除当前数据 <span class="color-red" v-text="data.select.id"></span>？
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-default" data-dismiss="modal">
                            <i class="glyphicon glyphicon-remove mr-5"></i>关闭
                        </button>
                        <button @click="request('delete_data')" type="button" class="btn btn-default">
                            <i class="glyphicon glyphicon-trash mr-5"></i>删除
                        </button>
                    </div>
                </div>
            </div>
        </div>

        <message-popup ref="popup"></message-popup>

    </div>
</template>

<script>
import InputComp from "../components/input_comp/InputComp.vue";
import TableComp from '../components/container_comp/TableComp.vue';
import LoadingComp from "../components/LoadingComp.vue";
import MessagePopup from "../components/MessagePopup.vue";

export default {
    name: "List",
    components: {
        InputComp,
        TableComp,
        LoadingComp,
        MessagePopup
    },
    data() {
        return {
            info: {},
            data: {
                status: 1,  // 0: 正在加载中, 1: 加载完毕
                list: [],
                select: {}
            },
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
                data: [],
                total: 0
            },
            show: { param: {} },
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
                },
                search: {}
            }
        }
    },
    created() {
        let _this = this;

        this.info.table = this.$route.params.table;
        this.$nextTick(() => {
            _this.setHeight();
            _this.request("get_config");
        });

    },
    watch: {
        $route() {
            console.log(this.$route);
            this.info.table = this.$route.params.table;
            this.request("get_config");
        }
    },
    methods: {
        setHeight() {
            let height = document.documentElement.clientHeight;
            document.getElementById("app").style.height = (height - 1) + "px";
            $(".data-area").height(height - 271);
        },
        selectDataTitleKey(dataList) {
            const showTitle = this.info.show.param;

            for (let i = 0, len = dataList.length; i < len; i++) {
                if (dataList[i].key === showTitle) {
                    const copyTitleConf = [
                        { name: "ID", width: "30%" },
                        { name: "修改时间", width: "15%" },
                    ];

                    copyTitleConf.push({
                        name: dataList[i].name,
                        width: "55%"
                    });
                    this.table.titleConf = copyTitleConf;
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
                    { name: "date", value: data.date.modify, hidden: false },
                    { name: this.show.param.key, value: data.data[this.show.param.key], hidden: false }
                ])
            }
            return tableDataList;
        },
        request(type) {
            let _this = this;

            if (type === "get_config") {
                $.ajax({
                    method: "POST",
                    url: "http://192.168.121.127:6869/api/config/get",
                    headers: {
                        "Content-Type": "application/json",
                        "token": sessionStorage.getItem("token")
                    },
                    dataType: "JSON",
                    data: JSON.stringify({
                        table: this.info.table
                    }),
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
                this.data.status = 0;
                setTimeout(() => {
                    $.ajax({
                        method: "GET",
                        url: "http://192.168.121.127:6869/data/list",
                        headers: {
                            "token": sessionStorage.getItem("token")
                        },
                        data: {
                            table: this.info.table,
                            query: JSON.stringify(this.input.search),
                            offset: (this.input.page.current - 1) * this.input.page.limit,
                            limit: this.input.page.limit
                        },
                        success(resp) {
                            _this.data.status = 1;
                            if (resp.code === 1) {
                                _this.data.list = resp.data.list;
                                _this.table.data = _this.setTableData(resp.data.list);
                                _this.table.total = resp.data.count;
                            }

                        }
                    })
                }, 1000);
            }
            else if (type === "delete_data") {
                $("#modalDelete").modal("hide");
                this.$refs.popup.open("default", "正在删除数据中，请稍等......");

                setTimeout(() => {
                    $.ajax({
                        method: "POST",
                        url: "http://192.168.121.127:6869/data/delete",
                        headers: {
                            "Content-Type": "application/json",
                            "token": sessionStorage.getItem("token")
                        },
                        dataType: "JSON",
                        data: JSON.stringify({
                            table: this.info.table,
                            id: this.data.select.id
                        }),
                        success(resp) {
                            if (resp.code === 1) {
                                _this.$refs.popup.setAll("success", resp.msg);
                                _this.request("get_data_list");
                                setTimeout(() => {
                                    _this.$refs.popup.close();
                                }, 3000);
                            } else {
                                _this.$refs.popup.setAll("error", resp.msg);
                            }
                        },
                        error(err) {
                            _this.$refs.popup.setAll("error", err.statusText);
                        }
                    });
                }, 1000);
            }
        },
        search(paramDict) {
            this.input.search = paramDict;
            this.request("get_data_list");
        },
        tableHandle(data) {
            const method = data.method;

            if (method === "refresh") {
                this.request("get_data_list");
            }
            else if (method === "add") {
                this.$router.push("/detail/" + this.info.table + "/add/1");
            }
            else if (method === "table") {
                const type = data.type;

                this.data.select = { ...this.data.list[data.idx] };

                if (type === "edit") {
                    this.$router.push("/detail/" + this.info.table + "/edit/" + this.data.select.id);
                }
                else if (type === "del") {
                    $("#modalDelete").modal({
                        backdrop: "static"
                    });
                }
            }
            else if (method === "skip") {
                this.input.page = data.page;
                this.request("get_data_list");
            }
            else if (method === "limit") {
                this.input.page.limit = data.page.limit;
                this.request("get_data_list");
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
            position: relative;
            width: 100%;
            margin-top: 20px;
            border-top: 1px solid rgba(0, 0, 0, 0.1);
        }

    }
}
</style>