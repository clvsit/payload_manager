<template>
    <div id="InputBasicCompArea" class="input-area">
        <form v-on:keyup.enter="search" :id="formId" class="form-inline input-box">
            <div v-for="(item, idx) in inputList" :key="idx">
                <div v-if="item.type === 'text'" class="form-group mr-10">
                    <label class="control-label" v-text="item.title + '：'"></label>
                    <input type="text" class="form-control" :placeholder="item.placeholder" :data-name="item.name" />
                </div>
                <div v-else-if="item.type === 'text-small'" class="form-group mr-10">
                    <label class="control-label" v-text="item.title + '：'"></label>
                    <input type="text" class="form-control" :placeholder="item.placeholder" :data-name="item.name" style="width: 100px;" />
                </div>
                <div v-else-if="item.type === 'dateRange'" class="form-group mr-10" :id="'input' + idx">
                    <label class="control-label" v-text="item.title + '：'"></label>
                    <input type="date" class="form-control" :data-name="item.name + '-start'" />
                    &nbsp; - &nbsp;
                    <input type="date" class="form-control" :data-name="item.name + '-end'" />
                    <div v-if="item.helper" class="btn-group ml-10">
                        <div @click="helpSetDateRange('today', $event)" class="btn btn-default">今日</div>
                        <div @click="helpSetDateRange('yesterday', $event)" class="btn btn-default">昨日</div>
                        <div @click="helpSetDateRange('week', $event)" class="btn btn-default">近一周</div>
                        <div @click="helpSetDateRange('month', $event)" class="btn btn-default">近一月</div>
                    </div>

                </div>
                <div v-else-if="item.type === 'datetimeRange'" class="form-group mr-10">
                    <label class="control-label" v-text="item.title + '：'"></label>
                    <input type="datetime-local" class="form-control" :data-name="item.name + '-start'" />
                    &nbsp; - &nbsp;
                    <input type="datetime-local" class="form-control" :data-name="item.name + '-end'" />
                </div>
                <div v-else-if="item.type === 'select'" class="form-group mr-10">
                    <label class="control-label" v-text="item.title + '：'"></label>
                    <select class="form-control" :data-name="item.name">
                        <option :value="sItem.value" v-for="(sItem, sIdx) in item.select" :key="sIdx"
                            v-text="sItem.name"></option>
                    </select>
                </div>

            </div>
        </form>
        <div class="btn-group input-btn-group">
            <div @click="search" class="btn btn-default">
                <i class="glyphicon glyphicon-search"></i>
                检索
            </div>
            <div @click="clear" class="btn btn-default">
                <i class="glyphicon glyphicon-fire"></i>
                清空
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "InputBasic",
    props: ["inputList", "name", "width"],
    data() {
        return {
            formId: "default"
        }
    },
    created() {
        let _this = this;

        this.$nextTick(() => {
            _this.formId = !_this.name ? "default" : _this.name;

            if (_this.width) {
                $("#InputBasicCompArea").css("width", Number(_this.width));
            }
        });
    },
    methods: {
        search() {
            let paramDict = {},
                $form = $("#" + this.formId);

            $form.find("input").each(function () {
                let name = $(this).attr("data-name");
                let value = $(this).val();
                if (value) {
                    paramDict[name] = value;
                }
            });
            $form.find("select").each(function () {
                let name = $(this).attr("data-name");
                let value = $(this).val();
                if (value) {
                    paramDict[name] = value;
                }
            });
            this.$emit("search", paramDict);
        },
        clear() {
            let paramDict = {},
                $form = $("#" + this.formId);

            $form.find("input").each(function () {
                $(this).val("");
            });
            $form.find("select").each(function () {
                $(this).val("");
            });
            this.$emit("search", paramDict);
        },
        helpSetDateRange(type, event) {
            const today = new Date(),
                id = $(event.target).parents(".form-group").eq(0).attr("id"),
                $dom = $("#" + id),
                $domStart = $dom.find("input").eq(0),
                $domEnd = $dom.find("input").eq(1);
            let start = null,
                end = today.getFullYear() + "-" + (today.getMonth() + 1 >= 10 ? today.getMonth() + 1 : "0" + (today.getMonth() + 1)) + "-" + today.getDate();

            if (type === "today") {
                start = this.addOrReduceDate("D", end, -1);
                $domStart.val(start);
                $domEnd.val(end);
            }
            else if (type === "yesterday") {
                start = this.addOrReduceDate("D", end, -2);
                end = this.addOrReduceDate("D", end, -1);
                $domStart.val(start);
                $domEnd.val(end);
            }
            else if (type === "week") {
                start = this.addOrReduceDate("D", end, -7);
                $domStart.val(start);
                $domEnd.val(end);
            }
            else if (type === "month") {
                start = this.addOrReduceDate("M", end, -1);
                $domStart.val(start);
                $domEnd.val(end);
            }
        },
        addOrReduceDate(type, date, num) {
            var nowDate = null;
            var strDate = "";
            num = parseInt(num); // 防止传入字符串报错
            var seperator1 = "-";
            if (date == "") {
                nowDate = new Date();
            } else {
                nowDate = new Date(date);
            }

            if (type === "Y") {
                nowDate.setFullYear(nowDate.getFullYear() + num);
            }
            if (type === "M") {
                nowDate.setMonth(nowDate.getMonth() + num);
            }
            if (type === "D") {
                nowDate.setDate(nowDate.getDate() + num);
            }
            if (type === "A") {
                nowDate.setFullYear(nowDate.getFullYear() + num);
                nowDate.setMonth(nowDate.getMonth() + num);
                nowDate.setDate(nowDate.getDate() + num);
            }
            var year = nowDate.getFullYear(); // 年
            var month = nowDate.getMonth() + 1; // 月
            strDate = nowDate.getDate(); //日
            if (month >= 1 && month <= 9) {
                month = "0" + month;
            }
            if (strDate >= 0 && strDate <= 9) {
                strDate = "0" + strDate;
            }
            var dateStr = year + seperator1 + month + seperator1 + strDate
            console.log(dateStr)
            return dateStr;
        }
    }
}
</script>

<style lang="scss" scoped>
.input-area {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    padding: 0 10px;

    .form-inline {
        display: flex;
        flex-direction: row;
        flex-wrap: wrap;
        justify-content: flex-start;

        .form-group {
            margin-bottom: 10px;
        }
    }

    .input-box {
        // width: 80%;
        width: calc(100% - 170px);
        // min-width: 1100px;
    }

    .input-btn-group {
        min-width: 170px;
        display: flex;
        flex-direction: row;
        justify-content: flex-end;

        .btn {
            height: 34px;
        }
    }
}
</style>