<template>
    <div class="body">
        <left-sidebar-comp></left-sidebar-comp>
        <div class="right-container">
            <div class="right-header">
                <nav class="navbar">
                    <!-- <ol class="breadcrumb">
            <li><a href="#">Home</a></li>
            <li><a href="#/list?title=个人信息">个人信息</a></li>
            <li class="active">Data</li>
          </ol> -->
                    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                        <i @click="this.$router.back();" class="glyphicon glyphicon-share-alt btn-back" data-toggle="tooltip" data-placement="right" title="返回"></i>
                        <ul class="nav navbar-nav navbar-right">
                            <li class="dropdown">
                                <div class="avatar" data-toggle="dropdown" role="button" aria-haspopup="true"
                                    aria-expanded="false">
                                    <i class="glyphicon glyphicon-user"></i>
                                </div>
                                <ul class="dropdown-menu">
                                    <li><a href="#">暂未实现</a></li>
                                    <li role="separator" class="divider"></li>
                                    <li @click="logout"><a href="javascript:;">注销账户</a></li>
                                </ul>
                            </li>
                        </ul>
                    </div><!-- /.navbar-collapse -->

                </nav>
            </div>
            <div class="right-body">
                <router-view v-slot="{ Component }">
                    <transition name="fade" mode="out-in">
                        <component :is="Component" />
                    </transition>
                </router-view>
            </div>
        </div>

        <message-popup ref="popup"></message-popup>

    </div>
</template>

<script>
import LeftSidebarComp from "@/components/container_comp/LeftSidebarComp.vue"
import MessagePopup from "../components/MessagePopup.vue";

export default {
    name: 'Home',
    components: {
        LeftSidebarComp,
        MessagePopup
    },
    data() {
        return {

        }
    },
    created() {
        let _this = this;

        this.$nextTick(() => {
            _this.setHeight();
            _this.request("check_login");
        });

        window.onresize = () => {
            _this.setHeight();
        }
    },
    methods: {
        setHeight() {
            let height = document.documentElement.clientHeight;
            document.getElementById("app").style.height = (height - 1) + "px";
            $(".right-body").height(height - 101);
        },
        logout() {
            let _this = this;

            $.ajax({
                method: "POST",
                url: "http://192.168.121.127:6869/api/logout",
                headers: {
                    "Content-Type": "application/json"
                },
                dataType: "JSON",
                data: JSON.stringify({
                    token: sessionStorage.getItem("token")
                }),
                success(resp) {
                    _this.$router.replace("/login");
                    sessionStorage.removeItem("token");
                },
                error(err) {
                    _this.$router.replace("/login");
                }
            })
        },
        request(type) {
            let _this = this;

            if (type === "check_login") {
                $.ajax({
                    method: "POST",
                    url: "http://192.168.121.127:6869/api/user/check",
                    headers: {
                        "Content-Type": "application/json",
                        "token": sessionStorage.getItem("token")
                    },
                    dataType: "JSON",
                    data: JSON.stringify({
                        token: sessionStorage.getItem("token")
                    }),
                    success(resp) {
                        if (resp.code === 1) {

                        } else {
                            _this.$refs.popup.open("error", "用户未登录，或登录状态过期，请重新登录哦！");
                            setTimeout(() => {
                                _this.$refs.popup.close();
                                _this.$router.replace("/login");
                            }, 2000);
                        }
                    }
                });
            }
        }
    },
}
</script>

<style lang="scss" scoped>
.right-body::-webkit-scrollbar {
    width: 4px;
}

.right-body::-webkit-scrollbar-thumb {
    border-radius: 10px;
    box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.2);
    background: rgba(0, 0, 0, 0.2);
}

.right-body::-webkit-scrollbar-track {
    box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.2);
    border-radius: 0;
    background: rgba(0, 0, 0, 0.1);
}

.right-container {
    width: calc(100% - 299px);
    height: 100%;
    background-color: #fff;

    .right-header {
        width: 100%;
        height: 60px;
        border-bottom: 1px solid rgba(0, 0, 0, 0.1);

        .navbar {
            // display: flex;
            // flex-direction: row;
            // justify-content: space-between;
        }

        .breadcrumb {
            width: 90%;
            height: 100%;
            line-height: 40px;
            margin-bottom: 0;
            background-color: #fff;
        }

        .btn-back {
            position: relative;
            top: 15px;
            left: 10px;
            font-size: 24px;
            transform: rotateY(180deg);
            cursor: pointer;
        }


        .avatar {
            width: 40px;
            height: 40px;
            margin-top: 10px;
            margin-right: 20px;
            border-radius: 20px;
            box-shadow: 0 0 2px 1px rgba(0, 0, 0, 0.3);
            text-align: center;
            transition: all 0.5s ease-in-out;

            i {
                font-size: 26px;
                line-height: 40px;
            }
        }

        .avatar:hover {
            transform: scale(1.1, 1.1);
            box-shadow: 0 0 3px 2px rgba(0, 0, 0, 0.7);
        }
    }

    .right-body {
        padding: 10px 20px;
        overflow: auto;
    }
}

.fade-enter-active, .fade-leave-active {
  transition: opacity .5s;
}

.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
</style>