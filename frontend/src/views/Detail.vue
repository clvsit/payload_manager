<template>
    <div class="payload-detail">

        <div class="payload-detail-header">
            <div class="btn btn-default"></div>
            <h3 v-text="title"></h3>
        </div>

        <div class="payload-detail-body">
            <div class="btn-group">
                <div class="btn btn-default">
                    <i class="glyphicon glyphicon-plus"></i>
                    添加
                </div>
                <div class="btn btn-default">
                    <i class="glyphicon glyphicon-refresh"></i>
                    清空
                </div>
            </div>
            <div class="row mt-20">
                <div class="col-md-7">
                    <form class="form">

                        <div class="form-group" v-for="(item, idx) in inputList" :key="idx">
                            <div v-if="item.type === 'text'">
                                <label class="control-label" v-text="item.name"></label>
                                <input v-model="item.input" type="text" class="form-control" />
                            </div>
                            <div v-else-if="item.type === 'number'">
                                <label class="control-label" v-text="item.name"></label>
                                <input v-model="item.input" type="number" class="form-control" />
                            </div>
                            <div v-else-if="item.type === 'select'">
                                <label class="control-label" v-text="item.name"></label>
                                <select v-model="item.input" class="form-control">
                                    <option value="optionItem.value" v-for="optionItem in item.optionList"
                                        :key="optionItem.key" v-text="optionItem.key"></option>
                                </select>
                            </div>
                        </div>
                    </form>
                </div>
                <div class="col-md-5">
                    <form class="form">
                        <div class="form-group">
                            <label class="control-label">YAML 格式</label>
                            <textarea class="form-control"></textarea>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "Detail",
    data() {
        return {
            inputList: [],
            title: ""
        }
    },
    created() {
        let _this = this;

        this.title = this.$route.query.title;
        this.$nextTick(() => {
            _this.request("get_config");
        });
    },
    methods: {
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
                        let inputList = [];

                        if (resp.code === 1) {
                            for (let i = 0, len = detailDict.data.length; i < len; i++) {
                                inputList.push({
                                    ...detailDict.data[i],
                                    input: detailDict.data[i].default,
                                });
                            }
                        }
                        _this.inputList = inputList;
                    }
                })
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
    }
}
</style>