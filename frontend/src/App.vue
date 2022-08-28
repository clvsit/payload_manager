<template>
  <div class="body">
    <left-sidebar-comp></left-sidebar-comp>
    <div class="right-container">
      <div class="right-header">
        
      </div>
      <div class="right-body">
        <router-view />
      </div>
    </div>
  </div>
</template>

<style lang="scss">
// @import "@/assets/style/base.scss";

.body {
  display: flex;
  flex-direction: row;
  height: 100%;
  // background-color: #f5f7fb;
}

.right-container {
  width: calc(100% - 299px);
  height: 100%;
  background-color: #fff;

  .right-header {
    width: 100%;
    height: 60px;
    border-bottom: 1px solid rgba(0, 0, 0, 0.1);
    // box-shadow: 0 0 3px 2px rgba(0, 0, 0, 0.3);
  }

  .right-body {
    padding: 10px 20px;
    overflow: auto;
  }
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