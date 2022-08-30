<template>
    <div>
        <div class="container">
            <div class="login-header">
                <h3>登录界面</h3>
            </div>
            <div class="login-body">
                <form class="form">
                    <div class="form-group">
                        <label class="control-label">用户账号：</label>
                        <input type="text" class="form-control" />
                    </div>
                    <div class="form-group">
                        <label class="control-label">用户密码：</label>
                        <input type="password" class="form-control" />
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
    </div>
</template>

<script>
export default {
    name: "Login",
    methods: {
        login() {
            this.$router.push("/");
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