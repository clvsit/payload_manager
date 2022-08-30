<template>
    <div :id="popupId" class="modal fade" role="dialog">
        <div class="modal-dialog" role="document">
            <div class="alert" :class="type" role="alert" v-html="message"></div>
        </div>
    </div>
</template>

<script>
export default {
    name: "MessagePopup",
    props: ["id"],
    data() {
        return {
            popupId: "msgPopDefault",
            type: "alert-default",
            message: ""
        }
    },
    created() {
        let _this = this;

        this.$nextTick(() => {
            _this.popupId = !_this.id ? "msgPopDefault" : _this.id;
        });
    },
    methods: {
        setType(type) {
            switch (type) {
                case "success": {
                   this.type = "alert-success";
                   break;
                }
                case "error": {
                    this.type = "alert-danger";
                    break;
                }
                default: {
                    this.type = "alert-default";
                    break;
                }
            }
        },
        setMessage(message) {
            this.message = message;
        },
        setAll(type, message) {
            this.setType(type);
            this.setMessage(message);
        },
        open(type, message) {
            this.setType(type);
            this.message = message;
            $("#" + this.popupId).modal("show");
        },
        close() {
            this.setType("default");
            this.message = "";
            $("#" + this.popupId).modal("hide");
        },
    }
}
</script>

<style lang="scss" scoped>
.alert-default {
  color: #070707;
  background-color: #f9ffff;
  box-shadow: 0 0 5px 3px rgb(0 0 0 / 30%);
}
</style>