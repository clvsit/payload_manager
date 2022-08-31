<template>
    <div>
        <div @keyup.enter="login" class="container">
            <div class="login-header">
                <h3>登录界面</h3>
            </div>
            <div class="login-body">
                <form class="form">
                    <div class="form-group">
                        <label class="control-label">用户账号：</label>
                        <input v-model="username" type="text" class="form-control" />
                    </div>
                    <div class="form-group">
                        <label class="control-label">用户密码：</label>
                        <input v-model="password" type="password" class="form-control" />
                    </div>
                    <div class="form-group text-center btn-login">
                        <div @click="login" class="btn btn-default">登录</div>
                    </div>
                </form>
            </div>
        </div>
        <div class="background">
            <!-- <img src="~@/assets/images/background2.jpg" /> -->
        </div>

        <message-popup ref="popup"></message-popup>

    </div>
</template>

<script>
import MessagePopup from "../components/MessagePopup.vue";

export default {
    name: "Login",
    components: {
        MessagePopup
    },
    data() {
        return {
            username: "",
            password: ""
        }
    },
    methods: {
        login() {
            let _this = this;

            this.$refs.popup.open("default", "正在登录中，请稍等......");

            setTimeout(() => {
                $.ajax({
                    method: "POST",
                    url: "http://192.168.121.127:6869/api/login",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    dataType: "JSON",
                    data: JSON.stringify({
                        username: this.username,
                        password: this.password
                    }),
                    success(resp) {
                        if (resp.code === 1) {
                            _this.$refs.popup.setAll("success", resp.msg);
                            sessionStorage.setItem("token", resp.data.token);
                            sessionStorage.setItem("role", resp.data.role);
                            setTimeout(() => {
                                _this.$refs.popup.close();
                                _this.$router.push("/dashboard");
                            }, 1000);
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
    }
}
</script>

<style lang="scss" scoped>
.container {
    position: fixed;
    top: 50%;
    left: 50%;
    width: 800px;
    height: 500px;
    margin-top: -250px;
    margin-left: -400px;
    border-radius: 20px;
    box-shadow: 2px 3px 5px 3px rgba(0, 0, 0, 0.3);
    background-color: #fff;

    .login-header {
        width: 100%;
        height: 50px;
        border-bottom: 1px solid rgba(0, 0, 0, 0.1);
        padding-left: 10px;
    }

    .login-body {
        width: 100%;
        margin-top: 20px;
        padding: 50px 10px 20px;

        .form-group {
            margin-bottom: 30px;
        }

        .btn-login {
            width: 100%;
            margin-top: 100px;

            .btn {
                width: 200px;
            }
        }
    }
}

.background {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -1;
    background: url("~@/assets/images/background2.jpg") center center no-repeat;
    background-color: #000;

    img {
        height: 100%;
    }
}
</style>