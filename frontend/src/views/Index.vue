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
                        <!-- <div class="btn btn-default mt-10">
              <i class="glyphicon glyphicon-share-alt"></i>
            </div> -->
                        <ul class="nav navbar-nav navbar-right">
                            <li class="dropdown">
                                <div class="avatar" data-toggle="dropdown" role="button" aria-haspopup="true"
                                    aria-expanded="false">
                                </div>
                                <ul class="dropdown-menu">
                                    <li><a href="#">Action</a></li>
                                    <li><a href="#">Another action</a></li>
                                    <li><a href="#">Something else here</a></li>
                                    <li role="separator" class="divider"></li>
                                    <li><a href="#/login">注销账户</a></li>
                                </ul>
                            </li>
                        </ul>
                    </div><!-- /.navbar-collapse -->

                </nav>
            </div>
            <div class="right-body">
                <router-view />
            </div>
        </div>
    </div>
</template>

<script>
import LeftSidebarComp from "@/components/container_comp/LeftSidebarComp.vue"

export default {
    name: 'Home',
    components: {
        LeftSidebarComp
    },
    created() {
        let _this = this;

        this.$nextTick(() => {
            _this.setHeight();
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
</style>