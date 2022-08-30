<template>
  <router-view></router-view>
</template>

<style lang="scss">
// @import "@/assets/style/base.scss";

.body {
  display: flex;
  flex-direction: row;
  height: 100%;
  // background-color: #f5f7fb;
}

.mt-20 {
  margin-top: 20px !important;
}

.mr-5 {
  margin-right: 5px !important;
}

.mr-10 {
  margin-right: 10px !important;
}

.mr-20 {
  margin-right: 20px !important;
}

.pl-10 {
  padding-left: 10px !important;
}

.ellipsis {
  // width: 400px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.color-red {
  color: #f00;
}
</style>

<script>
import LeftSidebarComp from "@/components/container_comp/LeftSidebarComp.vue"

export default {
  name: 'App',
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