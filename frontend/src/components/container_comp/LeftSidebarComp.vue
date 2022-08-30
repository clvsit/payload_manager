<template>
    <div class="left-sidebar">
        <div class="left-header">
            <h1 class="text-center">
                <!-- <img style="width: 30px; background-color: #fff;" src="~@/assets/images/brand.png" /> -->
                PayLoad
            </h1>
        </div>
        <div class="left-body">
            <div @click="choose" class="left-nav">
                <div class="left-nav-group" v-for="(nav, nIdx) in navList" :key="nIdx">
                    <div class="left-nav-group-name">
                        <div v-text="nav.name"></div>
                    </div>
                    <ul class="left-nav-group-list">
                        <li class="left-nav-group-item" v-for="(item, idx) in nav.group" :key="idx" :data-url="item.url">
                            <span v-text="item.name"></span>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

export default {
    name: 'LeftSiderbarComp',
    data() {
        return {
            navList: []
        }
    },
    created() {
        let _this = this;

        this.$nextTick(() => {
            _this.request("get_config_list");
        });
    },
    methods: {
        choose(event) {
            const target = event.target;
            let urlEle = null;

            $(".left-nav-group-item-click").removeClass("left-nav-group-item-click");

            if (target.tagName === "I" || target.tagName === "SPAN") {
                urlEle = target.parentElement;
                this.$router.push(urlEle.getAttribute("data-url"));
                urlEle.classList.add("left-nav-group-item-click");
            } else if (target.tagName === "LI") {
                urlEle = target;
                this.$router.push(urlEle.getAttribute("data-url"));
                urlEle.classList.add("left-nav-group-item-click");
            }
        },
        request(type) {
            let _this = this;

            if (type === "get_config_list") {
                const token = sessionStorage.getItem("token");

                $.ajax({
                    method: "POST",
                    url: "http://192.168.121.127:6869/config/list",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    dataType: "JSON",
                    data: JSON.stringify({
                        token: token
                    }),
                    success(resp) {
                        if (resp.code === 1) {
                            _this.navList = resp.data.list;
                        }
                    }
                })
            }
        }
    }
}
</script>


<style lang="scss" scoped>
.left-sidebar {
    position: relative;
    display: flex;
    flex-direction: column;
    width: 300px;
    height: 100%;
    padding: 10px;
    border-right: 1px solid rgba(0, 0, 0, 0.1);
    background-color: #fff;
    // box-shadow: 0 0 3px 2px rgb(0 0 0 / 10%);
    z-index: 1;

    .left-header {
        width: 100%;
        height: 100px;
        border-bottom: 1px solid rgba(0, 0, 0, 0.1);
    }

    .left-body {
        width: 100%;
        height: auto;
        margin-top: 20px;
        overflow: auto;

        .left-nav {

            .left-nav-group {

                .left-nav-group-name {
                    display: flex;
                    flex-direction: row;
                    justify-content: space-between;
                    height: 40px;
                    line-height: 40px;
                    font-size: 16px;
                    font-weight: bold;
                    padding-left: 20px;
                    cursor: pointer;
                    transition: all 0.5s cubic-bezier(0.39, 0.575, 0.565, 1);
                }

                .left-nav-group-list {
                    list-style: None;
                    padding-left: 0;

                    .left-nav-group-item {
                        height: 30px;
                        line-height: 30px;
                        padding-left: 40px;
                        cursor: pointer;
                        transition: all 0.5s cubic-bezier(0.39, 0.575, 0.565, 1);
                    }

                    // .left-nav-group-item:hover {
                    //     background-color: #eee;
                    // }

                    .left-nav-group-item-click {
                        background-color: #fff;
                        color: #000;
                        border-radius: 5px;
                    }
                }
            }
        }
    }

    .left-body::-webkit-scrollbar {
        width: 4px;
    }

    .left-body::-webkit-scrollbar-thumb {
        border-radius: 10px;
        box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.2);
        background: rgba(0, 0, 0, 0.2);
    }

    .left-body::-webkit-scrollbar-track {
        box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.2);
        border-radius: 0;
        background: rgba(0, 0, 0, 0.1);
    }
    
    .left-footer {
        position: absolute;
        bottom: 0;
        width: 180px;
        height: 70px;
        text-align: center;

        i {
            font-size: 32px;
            font-weight: bold;
            cursor: pointer;
        }
    }
}
</style>