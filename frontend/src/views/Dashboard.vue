<template>
    <div class="dashboard">
        <div class="dashboard-header">
            <h3>数据集合</h3>
        </div>

        <div class="dashboard-body">
            <div class="row" v-for="group in collectionList" :key="group.name">
                <div class="group-title" v-text="group.name"></div>
                <div class="col-md-12">
                    <div class="row">
                        <div class="col-sm-6 col-md-3" v-for="item in group.group" :key="item.id">
                            <div class="thumbnail">
                                <!-- <img src="~@/assets/images/no-content.jpeg" alt="..."> -->
                                <div class="caption">
                                    <h4 v-text="item.name"></h4>
                                    <p class="mt-10">
                                        <a :href="item.url" class="btn btn-default" role="button">
                                            <i class="glyphicon glyphicon-plus"></i>
                                        </a>
                                    </p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "Dashboard",
    data() {
        return {
            collectionList: []
        }
    },
    created() {
        let _this = this;

        this.$nextTick(() => {
            _this.request("get_config_list");
        });
    },
    methods: {
        request(type) {
            let _this = this;

            if (type === "get_config_list") {
                const token = sessionStorage.getItem("token");

                $.ajax({
                    method: "POST",
                    url: "http://192.168.121.127:6869/api/config/list",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    dataType: "JSON",
                    data: JSON.stringify({
                        token: token
                    }),
                    success(resp) {
                        if (resp.code === 1) {
                            _this.collectionList = resp.data.list;
                        }
                    }
                })
            }
        }
    }
}
</script>

<style lang="scss" scoped>
.dashboard {

    .dashboard-header {
        padding: 0 10px 10px;
        border-bottom: 2px dashed rgba(0, 0, 0, 0.1);
    }

    .dashboard-body {
        margin-top: 20px;

        .group-title {
            height: 50px;
            line-height: 50px;
            padding-left: 20px;
            font-size: 20px;
            font-weight: bold;
        }

        img {
            height: 200px;
        }
    }
}
</style>