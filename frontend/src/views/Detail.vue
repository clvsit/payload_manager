<template>
    <div class="payload-detail">

        <div class="payload-detail-header">
            <h3 v-if="param.type === 'add'" v-text="info.title"></h3>
            <h3 v-else-if="param.type === 'edit'" v-text="info.title + '：' + param.id"></h3>
        </div>

        <div class="payload-detail-body">

            <div id="inputArea" class="row mt-20">
                <div class="col-md-8 input-area">
                    <form class="form">

                        <div class="form-group" v-for="(item, idx) in inputList" :key="idx">
                            <div v-if="item.type === 'text'">
                                <label class="control-label">
                                    <span v-if="item.required" class="color-red">★</span>
                                    <span v-text="item.name"></span>
                                </label>
                                <input v-model="item.input" type="text" class="form-control" />
                            </div>
                            <div v-else-if="item.type === 'password'">
                                <label class="control-label">
                                    <span v-if="item.required" class="color-red">★</span>
                                    <span v-text="item.name"></span>
                                </label>
                                <input v-model="item.input" type="password" class="form-control" />
                            </div>
                            <div v-else-if="item.type === 'number'">
                                <label class="control-label">
                                    <span v-if="item.required" class="color-red">★</span>
                                    <span v-text="item.name"></span>
                                </label>
                                <input v-model="item.input" type="number" class="form-control" />
                            </div>
                            <div v-else-if="item.type === 'select'">
                                <label class="control-label">
                                    <span v-if="item.required" class="color-red">★</span>
                                    <span v-text="item.name"></span>
                                </label>
                                <select v-model="item.input" class="form-control">
                                    <option :value="optionItem.value" v-for="optionItem in item.optionList"
                                        :key="optionItem.text" v-text="optionItem.text"></option>
                                </select>
                            </div>
                            <div v-else-if="item.type === 'multiSelect'">
                                <label class="control-label">
                                    <span v-if="item.required" class="color-red">★</span>
                                    <span v-text="item.name"></span>
                                </label>
                                <div class="pl-10">
                                    <div class="checkbox" v-for="optionItem in item.optionList" :key="optionItem.text">
                                        <label>
                                            <input v-model="item.input" type="checkbox" :value="optionItem.value">
                                            <span v-text="optionItem.text"></span>
                                        </label>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </form>
                </div>
                <div class="col-md-4 info-area">
                    <div class="btn-group info-op-area">
                        <div v-if="param.type === 'add'" @click="request('add_data'); this.other.addStatus = 0;" class="btn btn-default">
                            <i class="glyphicon glyphicon-plus"></i>
                            添加后返回
                        </div>
                        <div v-if="param.type === 'add'" @click="request('add_data'); this.other.addStatus = 1;" class="btn btn-default">
                            <i class="glyphicon glyphicon-plus"></i>
                            添加后前往
                        </div>
                        <div v-else-if="param.type === 'edit'" @click="request('update_data')" class="btn btn-default">
                            <i class="glyphicon glyphicon-plus"></i>
                            保存
                        </div>
                        <div v-if="param.type === 'add'" @click="clear" class="btn btn-default">
                            <i class="glyphicon glyphicon-refresh"></i>
                            清空
                        </div>
                        <div v-if="param.type === 'edit'" @click="openPopup('copy')" class="btn btn-default">
                            <i class="glyphicon glyphicon-duplicate"></i>
                            复制
                        </div>
                        <div v-if="param.type === 'edit'" @click="openPopup('delete')" class="btn btn-default">
                            <i class="glyphicon glyphicon-trash"></i>
                            删除
                        </div>
                    </div>
                    <div v-if="param.type === 'edit'" class="info-list">
                        <div class="info-item">
                            <div class="info-item-name">
                                <span class="mr-5">API URL</span>
                                <i @click="copyAPIUrl" class="glyphicon glyphicon-copy icon-url-copy"
                                    data-toggle="tooltip" data-placemnt="top" :title="other.copyTitle"></i>
                            </div>
                            <div class="info-item-value">
                                <a id="apiUrl" class="ellipsis"
                                    :href="'http://localhost:6869/api/' + this.info.table + '/' + this.param.id"
                                    target="_blank"
                                    v-text="'http://localhost:6869/api/' + this.info.table + '/' + this.param.id"></a>
                            </div>
                        </div>
                        <div class="info-item">
                            <div class="info-item-name">修改日期</div>
                            <div class="info-item-value" v-text="data.date.modify"></div>
                        </div>
                        <div class="info-item">
                            <div class="info-item-name">创建日期</div>
                            <div class="info-item-value" v-text="data.date.create"></div>
                        </div>
                    </div>
                </div>
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
                            是否删除当前数据 <span class="color-red" v-text="info.id"></span>？
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

        <!-- 复制数据弹窗 -->
        <div id="modalCopy" class="modal fade" role="dialog">
            <div class="modal-dialog" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <h4 class="modal-title">复制数据</h4>
                    </div>
                    <div class="modal-body">
                        <div class="alert-message">
                            是否要复制当前数据 <span class="color-red" v-text="info.id"></span>？
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-default" data-dismiss="modal">
                            <i class="glyphicon glyphicon-remove mr-5"></i>关闭
                        </button>
                        <button @click="request('copy_data'); this.other.copyAndSkip = 0;" type="button"
                            class="btn btn-default">
                            <i class="glyphicon glyphicon-copy mr-5"></i>复制
                        </button>
                        <button @click="request('copy_data'); this.other.copyAndSkip = 1;" type="button"
                            class="btn btn-default">
                            <i class="glyphicon glyphicon-paste mr-5"></i>复制并前往
                        </button>
                    </div>
                </div>
            </div>
        </div>

        <message-popup ref="popup"></message-popup>

    </div>
</template>

<script>
import MessagePopup from "../components/MessagePopup.vue";

export default {
    name: "Detail",
    components: {
        MessagePopup
    },
    data() {
        return {
            info: {},
            data: {
                date: {}
            },
            inputList: [],
            param: {
                table: "",
                id: "",
                type: ""
            },

            // 其他变量设置
            other: {
                copyTitle: "拷贝 URL",
                addStatus: 0,
                copyAndSkip: 0
            }
        }
    },
    created() {
        let _this = this;

        this.param = {
            table: this.$route.params.table,
            id: this.$route.params.id,
            type: this.$route.params.type
        };
        this.$nextTick(() => {
            _this.setHeight();
            _this.request("get_config");
            $('[data-toggle="tooltip"]').tooltip();
        });
    },
    watch: {
        $route() {
            this.param = {
                table: this.$route.params.table,
                id: this.$route.params.id,
                type: this.$route.params.type
            };
            this.request("get_config");
        }
    },
    methods: {
        setHeight() {
            let height = document.documentElement.clientHeight;
            document.getElementById("app").style.height = (height - 1) + "px";
            $("#inputArea").height(height - 191);
        },
        clear() {
            for (let i = 0, len = this.inputList.length; i < len; i++) {
                const inputItem = this.inputList[i];

                if (inputItem.type === "multiSelect") {
                    inputItem.input = [];
                } else {
                    inputItem.input = "";
                }
            }
        },
        copyAPIUrl() {
            const inputDom = document.createElement('input');

            document.body.appendChild(inputDom);
            inputDom.setAttribute('value', "http://192.168.121.127:6869/api/" + this.info.table + "/" + this.param.id);
            inputDom.select();
            document.execCommand("copy"); // 执行浏览器复制命令
            if (document.execCommand('copy')) {
                document.execCommand('copy');
            }
            document.body.removeChild(inputDom);
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
                        table: this.param.table
                    }),
                    success(resp) {
                        const detailDict = resp.data.detail;
                        let inputList = [];

                        if (resp.code === 1) {
                            for (let i = 0, len = detailDict.data.length; i < len; i++) {
                                inputList.push({
                                    ...detailDict.data[i],
                                    input: detailDict.data[i].default
                                });
                            }
                            _this.info = detailDict;
                            _this.inputList = inputList;

                            if (_this.param.type === "edit") {
                                _this.request("get_data");
                            }
                        } else {
                            
                        }
                    }
                });
            }
            if (type === "get_data") {
                $.ajax({
                    method: "GET",
                    url: "http://192.168.121.127:6869/data/get",
                    headers: {
                        "token": sessionStorage.getItem("token")
                    },
                    data: {
                        table: this.info.table,
                        id: this.param.id
                    },
                    success(resp) {
                        if (resp.code === 1) {
                            const dataDict = resp.data.detail.data;

                            for (let i = 0, len = _this.inputList.length; i < len; i++) {
                                const inputItem = _this.inputList[i];

                                inputItem.input = dataDict[inputItem.key];
                            }
                            _this.data = resp.data.detail;
                        }
                    }
                })
            }
            else if (type === "add_data") {
                this.$refs.popup.open("default", "正在添加数据中，请稍等......");

                setTimeout(() => {
                    $.ajax({
                        method: "POST",
                        url: "http://192.168.121.127:6869/data/add",
                        headers: {
                            "Content-Type": "application/json",
                            "token": sessionStorage.getItem("token")
                        },
                        dataType: "JSON",
                        data: JSON.stringify({
                            table: this.info.table,
                            data: this.getInputData()
                        }),
                        success(resp) {
                            if (resp.code === 1) {
                                _this.$refs.popup.setAll("success", resp.msg);
                                setTimeout(() => {
                                    _this.$refs.popup.close();
                                    if (_this.other.addStatus === 0) {
                                        _this.$router.back();
                                    } else if (_this.other.addStatus === 1) {
                                        _this.$router.push("detail?type=edit&title=" + _this.title + "&id=" + resp.data.id);
                                    }
                                }, 2000);
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
            else if (type === "update_data") {
                this.$refs.popup.open("default", "正在保存数据中，请稍等......");

                setTimeout(() => {
                    $.ajax({
                        method: "POST",
                        url: "http://192.168.121.127:6869/data/update",
                        headers: {
                            "Content-Type": "application/json",
                            "token": sessionStorage.getItem("token")
                        },
                        dataType: "JSON",
                        data: JSON.stringify({
                            table: this.info.table,
                            id: this.param.id,
                            data: this.getInputData()
                        }),
                        success(resp) {
                            if (resp.code === 1) {
                                _this.$refs.popup.setAll("success", resp.msg);
                                setTimeout(() => {
                                    _this.$refs.popup.close();
                                }, 2000);
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
            else if (type === "copy_data") {
                $("#modalCopy").modal("hide");
                this.$refs.popup.open("default", "正在复制数据中，请稍等......");

                setTimeout(() => {
                    $.ajax({
                        method: "POST",
                        url: "http://192.168.121.127:6869/data/copy",
                        headers: {
                            "Content-Type": "application/json",
                            "token": sessionStorage.getItem("token")
                        },
                        dataType: "JSON",
                        data: JSON.stringify({
                            table: this.info.table,
                            id: this.param.id
                        }),
                        success(resp) {
                            if (resp.code === 1) {
                                _this.$refs.popup.setAll("success", resp.msg);
                                setTimeout(() => {
                                    _this.$refs.popup.close();
                                    if (_this.other.copyAndSkip === 1) {
                                        _this.$router.push("detail?type=edit&title=" + _this.title + "&id=" + resp.data.id);
                                    }
                                }, 2000);
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
                            id: this.param.id
                        }),
                        success(resp) {
                            if (resp.code === 1) {
                                _this.$refs.popup.setAll("success", resp.msg);
                                setTimeout(() => {
                                    _this.$refs.popup.close();
                                    _this.$router.back();
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
        getInputData() {
            let inputData = {};

            for (let i = 0, len = this.inputList.length; i < len; i++) {
                const inputItem = this.inputList[i];

                inputData[inputItem.key] = inputItem.input;
            }

            return inputData;
        },
        openPopup(type) {
            if (type === "delete") {
                $("#modalDelete").modal({
                    backdrop: "static"
                });
            } else if (type === "copy") {
                $("#modalCopy").modal({
                    backdrop: "static"
                });
            }
        }
    }
}
</script>

<style lang="scss" scoped>
.payload-detail {

    .payload-detail-header {
        padding: 0 10px 10px;
        border-bottom: 2px dashed rgba(0, 0, 0, 0.1);
    }

    .payload-detail-body {
        margin-top: 20px;

        .input-area {
            height: 100%;
            border-right: 1px solid rgba(0, 0, 0, 0.1);
        }

        .info-area {
            position: relative;
            height: 100%;
            padding: 10px 30px;

            .info-op-area {
                width: 100%;
                height: 50px;
            }

            .info-list {
                position: absolute;
                bottom: 20px;
                left: 30px;
                width: 90%;
                height: 200px;

                .info-item {
                    width: 100%;
                    height: 60px;
                    margin-top: 10px;

                    .info-item-name {
                        color: #aaa;
                        font-size: 16px;
                        // font-weight: bold;

                        .icon-url-copy {
                            cursor: pointer;
                        }
                    }

                    .info-item-value {
                        // width: 80%;
                        margin-top: 10px;
                        overflow: hidden;
                        text-overflow: ellipsis;
                        white-space: nowrap;

                        a {
                            width: 100%;
                        }
                    }
                }


            }
        }
    }
}
</style>