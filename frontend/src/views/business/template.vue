<template>
    <div class="payload-detail">

        <div class="payload-detail-header">
            <h3 v-if="param.type === 'add'">话术模板</h3>
            <h3 v-else-if="param.type === 'edit'" v-text="'话术模板：' + param.id"></h3>
        </div>

        <div class="payload-detail-body">

            <div id="inputRow" class="row mt-20">
                <div id="inputArea" class="col-md-8 input-area">
                    <form @change="listen" class="form">
                        <div class="input-group-custom">
                            <div class="input-group-header">
                                <div class="input-group-header">
                                    <h4 class="input-title">客户</h4>
                                    <div class="input-op-area">
                                        <!-- <i class="glyphicon glyphicon-refresh mr-10" data-toggle="tooltip"
                                            data-placement="top" title="清空"></i> -->
                                        <i v-if="setting.fold[0]" @click="setting.fold[0] = !setting.fold[0];"
                                            class="glyphicon glyphicon-chevron-up"></i>
                                        <i v-else @click="setting.fold[0] = !setting.fold[0];"
                                            class="glyphicon glyphicon-chevron-down"></i>
                                    </div>
                                </div>
                            </div>
                            <div v-if="setting.fold[0]">
                                <div class="form-group">
                                    <label class="control-label">
                                        <span>购买时间</span>
                                    </label>
                                    <div class="pl-10">
                                        <div class="checkbox">
                                            <label class="mr-10">
                                                <input v-model="input.客户.客户" type="checkbox" value="一周内">
                                                <span>一周内</span>
                                            </label>
                                            <label class="mr-10">
                                                <input v-model="input.客户.客户" type="checkbox" value="一个月内">
                                                <span>一个月内</span>
                                            </label>
                                            <label class="mr-10">
                                                <input v-model="input.客户.客户" type="checkbox" value="三个月内">
                                                <span>三个月内</span>
                                            </label>
                                            <label class="mr-10">
                                                <input v-model="input.客户.客户" type="checkbox" value="一年内">
                                                <span>一年内</span>
                                            </label>
                                            <label class="mr-10">
                                                <input v-model="input.客户.客户" type="checkbox" value="一年前">
                                                <span>一年前</span>
                                            </label>
                                            <label class="mr-10">
                                                <input v-model="input.客户.客户" type="checkbox" value="无">
                                                <span>无</span>
                                            </label>
                                        </div>
                                    </div>
                                </div>
                                <div class="row">
                                    <div class="form-group col-md-8 col-sm-12">
                                        <label class="control-label">
                                            <span>购买商品</span>
                                        </label>
                                        <input v-model="input.客户.购买商品" type="text" class="form-control" />
                                    </div>
                                    <div class="form-group col-md-4 col-sm-12">
                                        <label class="control-label">
                                            <span>客户类型</span>
                                        </label>
                                        <select v-model="input.客户.客户类型" class="form-control">
                                            <option value="老会员">老会员</option>
                                            <option value="新会员">新会员</option>
                                            <option value="无">无</option>
                                        </select>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="input-group-custom">
                            <div class="input-group-header">
                                <h4 class="input-title">品牌</h4>
                                <div class="input-op-area">
                                    <i v-if="setting.fold[1]" @click="setting.fold[1] = !setting.fold[1];"
                                        class="glyphicon glyphicon-chevron-up"></i>
                                    <i v-else @click="setting.fold[1] = !setting.fold[1];"
                                        class="glyphicon glyphicon-chevron-down"></i>
                                </div>
                            </div>
                            <div v-if="setting.fold[1]">
                                <div class="row">
                                    <div class="form-group col-md-8 col-sm-12">
                                        <label class="control-label">名称</label>
                                        <input v-model="input.品牌.名称" type="text" class="form-control" />
                                    </div>
                                    <div class="form-group col-md-4 col-sm-12">
                                        <label class="control-label">国家</label>
                                        <select v-model="input.品牌.国家" class="form-control">
                                            <option value="老会员">老会员</option>
                                            <option value="新会员">新会员</option>
                                            <option value="无">无</option>
                                        </select>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="input-group-custom">
                            <div class="input-group-header">
                                <h4 class="input-title">店铺</h4>
                                <div class="input-op-area">
                                    <!-- <i class="glyphicon glyphicon-refresh mr-10" data-toggle="tooltip"
                                        data-placement="top" title="清空"></i> -->
                                    <i v-if="setting.fold[2]" @click="setting.fold[2] = !setting.fold[2];"
                                        class="glyphicon glyphicon-chevron-up"></i>
                                    <i v-else @click="setting.fold[2] = !setting.fold[2];"
                                        class="glyphicon glyphicon-chevron-down"></i>
                                </div>
                            </div>
                            <div v-if="setting.fold[2]">
                                <div class="form-group">
                                    <label class="control-label">
                                        <span class="color-red">★</span>
                                        <span>名称</span>
                                    </label>
                                    <input v-model="input.店铺.名称" type="text" class="form-control" />
                                </div>
                                <div class="form-group">
                                    <label class="control-label">平台</label>
                                    <div class="pl-10">
                                        <div class="checkbox">
                                            <label class="mr-10">
                                                <input v-model="input.店铺.平台" type="checkbox" value="天猫">
                                                <span>天猫</span>
                                            </label>
                                            <label class="mr-10">
                                                <input v-model="input.店铺.平台" type="checkbox" value="淘宝">
                                                <span>淘宝</span>
                                            </label>
                                            <label class="mr-10">
                                                <input v-model="input.店铺.平台" type="checkbox" value="京东">
                                                <span>京东</span>
                                            </label>
                                            <label class="mr-10">
                                                <input v-model="input.店铺.平台" type="checkbox" value="拼多多">
                                                <span>拼多多</span>
                                            </label>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="input-group-custom">
                            <div class="input-group-header">
                                <h4 class="input-title">链接</h4>
                                <div class="input-op-area">
                                    <!-- <i class="glyphicon glyphicon-refresh mr-10" data-toggle="tooltip"
                                        data-placement="top" title="清空"></i> -->
                                    <i v-if="setting.fold[3]" @click="setting.fold[3] = !setting.fold[3];"
                                        class="glyphicon glyphicon-chevron-up"></i>
                                    <i v-else @click="setting.fold[3] = !setting.fold[3];"
                                        class="glyphicon glyphicon-chevron-down"></i>
                                </div>
                            </div>
                            <div v-if="setting.fold[3]" class="row">
                                <div class="form-group col-md-4 col-sm-12">
                                    <label class="control-label">类型</label>
                                    <select v-model="input.链接.类型" class="form-control">
                                        <option value="店铺">店铺</option>
                                        <option value="品牌">品牌</option>
                                        <option value="活动">活动</option>
                                        <option value="优惠券">优惠券</option>
                                        <option value="商品">商品</option>
                                        <option value="">无</option>
                                    </select>
                                </div>
                                <div class="form-group col-md-8 col-sm-12">
                                    <label class="control-label">URL</label>
                                    <input v-model="input.链接.url" type="text" class="form-control" />
                                </div>
                            </div>
                        </div>

                        <ul class="nav nav-tabs" role="tablist">
                            <li role="presentation" class="active"><a href="#小程序" data-toggle="tab">小程序</a></li>
                            <li role="presentation"><a href="#活动" data-toggle="tab">活动</a></li>
                            <li role="presentation"><a href="#回购礼" data-toggle="tab">回购礼</a></li>
                            <li role="presentation"><a href="#买赠" data-toggle="tab">买赠</a></li>
                            <li role="presentation"><a href="#积分礼" data-toggle="tab">积分礼</a></li>
                            <li role="presentation"><a href="#满赠" data-toggle="tab">满赠</a></li>
                            <li role="presentation"><a href="#购后抽奖" data-toggle="tab">购后抽奖</a></li>
                            <li role="presentation"><a href="#优惠券" data-toggle="tab">优惠券</a></li>
                        </ul>
                        <div class="tab-content mt-20">
                            <div role="tabpanel" class="tab-pane active" id="小程序">
                                <div class="input-group-custom">
                                    <div class="row">
                                        <div class="form-group col-md-4 col-sm-12">
                                            <label class="control-label">类型</label>
                                            <select v-model="input.小程序.类型" class="form-control">
                                                <option value="店铺">店铺</option>
                                                <option value="品牌">品牌</option>
                                                <option value="活动">活动</option>
                                                <option value="优惠券">优惠券</option>
                                                <option value="商品">商品</option>
                                                <option value="">无</option>
                                            </select>
                                        </div>
                                        <div class="form-group col-md-8 col-sm-12">
                                            <label class="control-label">关键词</label>
                                            <input v-model="input.小程序.关键词" type="text" class="form-control" />
                                        </div>
                                    </div>

                                    <div class="form-group">
                                        <label class="control-label">URL</label>
                                        <input v-model="input.小程序.url" type="text" class="form-control" />
                                    </div>
                                </div>
                            </div>
                            <div role="tabpanel" class="tab-pane" id="活动">
                                <div class="input-group-custom">
                                    <div class="row">
                                        <div class="form-group col-md-8 col-sm-12">
                                            <label class="control-label">名称</label>
                                            <input v-model="input.活动.名称" type="text" class="form-control" />
                                        </div>
                                        <div class="form-group col-md-4 col-sm-12">
                                            <label class="control-label">简称</label>
                                            <input v-model="input.活动.简称" type="text" class="form-control" />
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="form-group col-md-6 col-sm-12">
                                            <label class="control-label">开始日期</label>
                                            <input v-model="input.活动.开始日期" type="datetime-local" class="form-control" />
                                        </div>
                                        <div class="form-group col-md-6 col-sm-12">
                                            <label class="control-label">截止日期</label>
                                            <input v-model="input.活动.截止日期" type="datetime-local" class="form-control" />
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div role="tabpanel" class="tab-pane" id="回购礼">
                                <div class="input-group-custom">
                                    <div class="form-group">
                                        <label class="control-label">商品信息</label>
                                        
                                            <div class="form form-goods" v-for="(item, idx) in input.回购礼.商品信息" :key="idx">
                                                <div class="form-goods-header">
                                                    <i @click="removeGoods" class="glyphicon glyphicon-remove" :data-index="idx"></i>
                                                </div>
                                                <div class="form-group">
                                                    <label class="control-label">名称</label>
                                                    <input v-model="item.名称" type="text" class="form-control" />
                                                </div>
                                                <div class="form-group">
                                                    <label class="control-label">总价格</label>
                                                    <input v-model="item.总价格" type="text" class="form-control" />
                                                    <p class="help-block">单位是 "元", 不用写单位。也可以写成“单价*数量”的格式，如“79*3”，表示 SKU
                                                        单价 79 元,
                                                        数量为 3 个</p>
                                                </div>
                                                <div class="form-group">
                                                    <label class="control-label">总容量</label>
                                                    <input v-model="item.总容量" type="text" class="form-control" />
                                                </div>
                                                <div class="row">
                                                    <div class="form-group col-md-6 col-sm-12">
                                                        <label class="control-label">
                                                            <span>SKU 类型</span>
                                                        </label>
                                                        <select v-model="item.SKU类型" class="form-control">
                                                            <option value="商品">商品</option>
                                                            <option value="套装">套装</option>
                                                            <option value="小样">小样</option>
                                                            <option value="优惠券">优惠券</option>
                                                            <option value="">无</option>
                                                        </select>
                                                    </div>
                                                    <div class="form-group col-md-6 col-sm-12">
                                                        <label class="control-label">SKU 品类</label>
                                                        <select v-model="item.SKU品类" class="form-control">
                                                            <option value="化妆品">化妆品</option>
                                                            <option value="零食">零食</option>
                                                            <option value="卫衣">卫衣</option>
                                                            <option value="牛仔裤">牛仔裤</option>
                                                            <option value="N/A">N/A</option>
                                                            <option value="">无</option>
                                                        </select>
                                                    </div>
                                                </div>
                                                <div v-if="item.SKU类型 === '套装'" class="form-group">
                                                    <label class="control-label">套装件数</label>
                                                    <input v-model="套装件数" type="number" class="form-control" />
                                                </div>
                                            </div>
                                        <div class="table-op-area">
                                            <div @click="addGoods" class="btn btn-default"><i class="glyphicon glyphicon-plus"></i></div>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label class="control-label">赠品信息</label>
                                        <div class="form-group sr-only">
                                            <label class="control-label">
                                                <span>商品信息</span>
                                            </label>
                                            <div class="form form-goods">
                                                <div class="form-goods-header">
                                                    <i class="glyphicon glyphicon-remove"></i>
                                                </div>
                                                <div class="form-group">
                                                    <label class="control-label">名称</label>
                                                    <input type="text" class="form-control" />
                                                </div>
                                                <div class="form-group">
                                                    <label class="control-label">总价格</label>
                                                    <input type="text" class="form-control" />
                                                    <p class="help-block">单位是 "元", 不用写单位。也可以写成“单价*数量”的格式，如“79*3”，表示 SKU
                                                        单价 79 元,
                                                        数量为 3 个</p>
                                                </div>
                                                <div class="form-group">
                                                    <label class="control-label">总容量</label>
                                                    <input type="text" class="form-control" />
                                                </div>
                                                <div class="row">
                                                    <div class="form-group col-md-6 col-sm-12">
                                                        <label class="control-label">
                                                            <span>SKU 类型</span>
                                                        </label>
                                                        <select class="form-control">
                                                            <option value="店铺">商品</option>
                                                            <option value="品牌">套装</option>
                                                            <option value="活动">小样</option>
                                                            <option value="优惠券">优惠券</option>
                                                            <option value="">无</option>
                                                        </select>
                                                    </div>
                                                    <div class="form-group col-md-6 col-sm-12">
                                                        <label class="control-label">SKU 品类</label>
                                                        <select class="form-control">
                                                            <option value="化妆品">化妆品</option>
                                                            <option value="零食">零食</option>
                                                            <option value="卫衣">卫衣</option>
                                                            <option value="牛仔裤">牛仔裤</option>
                                                            <option value="N/A">N/A</option>
                                                            <option value="">无</option>
                                                        </select>
                                                    </div>
                                                </div>
                                                <div class="form-group">
                                                    <label class="control-label">套装件数</label>
                                                    <input type="number" class="form-control" />
                                                </div>
                                            </div>
                                            <p class="help-block"></p>
                                        </div>
                                        <div class="table-op-area">
                                            <div class="btn btn-default"><i class="glyphicon glyphicon-plus"></i></div>
                                        </div>
                                    </div>

                                    <div class="row mt-20">
                                        <div class="form-group col-md-6 col-sm-12">
                                            <label class="control-label">开始日期</label>
                                            <input v-model="input.回购礼.开始日期" type="datetime-local"
                                                class="form-control" />
                                        </div>
                                        <div class="form-group col-md-6 col-sm-12">
                                            <label class="control-label">截止日期</label>
                                            <input v-model="input.回购礼.截止日期" type="datetime-local"
                                                class="form-control" />
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label class="control-label">备注信息</label>
                                        <input v-model="input.回购礼.备注信息" type="text" class="form-control" />
                                    </div>
                                </div>
                            </div>
                            <div role="tabpanel" class="tab-pane" id="messages">...</div>
                            <div role="tabpanel" class="tab-pane" id="优惠券">
                                <div class="input-group-custom">
                                    <div class="input-group-header">
                                        <h4 class="input-title">优惠券</h4>
                                    </div>
                                    <div class="row">
                                        <div class="form-group col-md-4 col-sm-12">
                                            <label class="control-label">门槛金额</label>
                                            <input type="number" class="form-control" />
                                            <p class="help-block">满多少钱可以赠送</p>
                                        </div>
                                        <div class="form-group col-md-4 col-sm-12">
                                            <label class="control-label">减免金额</label>
                                            <input type="number" class="form-control" />
                                        </div>
                                        <div class="form-group col-md-4 col-sm-12">
                                            <label class="control-label">优先级</label>
                                            <select class="form-control">
                                                <option value="高">高</option>
                                                <option value="低">低</option>
                                            </select>
                                        </div>
                                    </div>

                                    <div class="form-group">
                                        <label class="control-label">备注信息</label>
                                        <input type="text" class="form-control" />
                                    </div>
                                </div>
                            </div>
                        </div>

                    </form>
                </div>
                <div class="col-md-4 info-area">
                    <div class="btn-group info-op-area">
                        <div v-if="param.type === 'add'" @click="request('add_data'); this.other.addStatus = 0;"
                            class="btn btn-default">
                            <i class="glyphicon glyphicon-plus"></i>
                            添加后返回
                        </div>
                        <div v-if="param.type === 'add'" @click="request('add_data'); this.other.addStatus = 1;"
                            class="btn btn-default">
                            <i class="glyphicon glyphicon-plus"></i>
                            添加后前往
                        </div>
                        <div v-else-if="param.type === 'edit'" @click="request('update_data')" class="btn btn-default">
                            <i class="glyphicon glyphicon-plus"></i>
                            保存
                        </div>
                        <div v-if="param.type === 'add'" @click="clear" class="btn btn-default">
                            <i class="glyphicon glyphicon-refresh"></i>
                            清空
                        </div>
                        <div v-if="param.type === 'edit'" @click="openPopup('copy')" class="btn btn-default">
                            <i class="glyphicon glyphicon-duplicate"></i>
                            复制
                        </div>
                        <div v-if="param.type === 'edit'" @click="openPopup('delete')" class="btn btn-default">
                            <i class="glyphicon glyphicon-trash"></i>
                            删除
                        </div>
                    </div>
                    <div v-if="param.type === 'edit'" class="info-list">
                        <div class="info-item">
                            <div class="info-item-name">
                                <span class="mr-5">API URL</span>
                                <i @click="copyAPIUrl" class="glyphicon glyphicon-copy icon-url-copy"
                                    data-toggle="tooltip" data-placemnt="top" :title="other.copyTitle"></i>
                            </div>
                            <div class="info-item-value">
                                <a id="apiUrl" class="ellipsis"
                                    :href="'http://localhost:6869/api/' + this.info.table + '/' + this.param.id"
                                    target="_blank"
                                    v-text="'http://localhost:6869/api/' + this.info.table + '/' + this.param.id"></a>
                            </div>
                        </div>
                        <div class="info-item">
                            <div class="info-item-name">修改日期</div>
                            <div class="info-item-value" v-text="data.date.modify"></div>
                        </div>
                        <div class="info-item">
                            <div class="info-item-name">创建日期</div>
                            <div class="info-item-value" v-text="data.date.create"></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- 删除数据弹窗 -->
        <div id="modalDelete" class="modal fade" role="dialog">
            <div class="modal-dialog" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <h4 class="modal-title">删除数据</h4>
                    </div>
                    <div class="modal-body">
                        <div class="alert-message">
                            是否删除当前数据 <span class="color-red" v-text="info.id"></span>？
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-default" data-dismiss="modal">
                            <i class="glyphicon glyphicon-remove mr-5"></i>关闭
                        </button>
                        <button @click="request('delete_data')" type="button" class="btn btn-default">
                            <i class="glyphicon glyphicon-trash mr-5"></i>删除
                        </button>
                    </div>
                </div>
            </div>
        </div>

        <!-- 复制数据弹窗 -->
        <div id="modalCopy" class="modal fade" role="dialog">
            <div class="modal-dialog" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <h4 class="modal-title">复制数据</h4>
                    </div>
                    <div class="modal-body">
                        <div class="alert-message">
                            是否要复制当前数据 <span class="color-red" v-text="info.id"></span>？
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-default" data-dismiss="modal">
                            <i class="glyphicon glyphicon-remove mr-5"></i>关闭
                        </button>
                        <button @click="request('copy_data'); this.other.copyAndSkip = 0;" type="button"
                            class="btn btn-default">
                            <i class="glyphicon glyphicon-copy mr-5"></i>复制
                        </button>
                        <button @click="request('copy_data'); this.other.copyAndSkip = 1;" type="button"
                            class="btn btn-default">
                            <i class="glyphicon glyphicon-paste mr-5"></i>复制并前往
                        </button>
                    </div>
                </div>
            </div>
        </div>

        <message-popup ref="popup"></message-popup>

    </div>
</template>

<script>
import MessagePopup from "@/components/MessagePopup.vue";
export default {
    name: "Detail",
    components: {
        MessagePopup
    },
    data() {
        return {
            info: {},
            data: {
                date: {}
            },
            configType: "",
            inputList: [],
            param: {
                table: "",
                id: "",
                type: ""
            },
            // 其他变量设置
            other: {
                copyTitle: "拷贝 URL",
                addStatus: 0,
                copyAndSkip: 0
            },
            input: {
                客户: { 客户: [], 购买商品: "", 客户类型: "" },
                品牌: { 名称: "", 国家: "" },
                店铺: { 名称: "", 平台: [] },
                链接: { 类型: "", url: "" },
                小程序: { 类型: "", 关键词: "", url: "" },
                活动: { 名称: "", 简称: "", 开始日期: "", 结束日期: "" },
                回购礼: { 商品信息: [], 赠品信息: [], 优先级: "高", 开始日期: "", 结束日期: "", 备注信息: "" },
                买赠: { 商品信息: [], 赠品信息: [], 优先级: "高", 开始日期: "", 结束日期: "", 备注信息: "" },
                积分礼: { 商品信息: [], 积分倍率: "", 兑换品信息: [], 优先级: "高", 开始日期: "", 结束日期: "", 备注信息: "" },
                满赠: { 门槛金额: "", 赠品信息: [], 优先级: "高", 开始日期: "", 结束日期: "", 备注信息: "" },
                购后抽奖: { 商品信息: [], 奖项: [], 优先级: "高", 开始日期: "", 结束日期: "", 备注信息: "" },
                优惠券: { 门槛金额: "", 减免: "", 优先级: "高", 开始日期: "", 结束日期: "", 备注信息: "" }
            },
            setting: {
                fold: [true, true, true, true, true]
            }
        }
    },
    created() {
        let _this = this;
        this.param = {
            table: this.$route.params.table,
            id: this.$route.params.id,
            type: this.$route.params.type
        };
        this.$nextTick(() => {
            _this.setHeight();
            $('[data-toggle="tooltip"]').tooltip();
        });
    },
    methods: {
        listen() {
            console.log(this.inputList);
            if (this.configType === "v1") {
                for (let i = 0, len = this.inputList.length; i < len; i++) {
                    const inputItem = this.inputList[i];
                    if (inputItem.condition) {
                        console.log(inputItem.condition);
                        if (eval("this." + inputItem.condition)) {
                            inputItem.isCond = true;
                        } else {
                            inputItem.isCond = false;
                        }
                    } else {
                        inputItem.isCond = true;
                    }
                }
            }

        },
        setHeight() {
            let height = document.documentElement.clientHeight;
            document.getElementById("app").style.height = (height - 1) + "px";
            $("#inputRow").height(height - 191);
            $("#inputArea").height(height - 191);
        },
        clear() {
            for (let i = 0, len = this.inputList.length; i < len; i++) {
                const groupItem = this.inputList[i];
                for (let j = 0, jLen = groupItem.data.length; j < jLen; j++) {
                    const inputItem = groupItem.data[j];
                    if (inputItem.type === "multiSelect") {
                        inputItem.input = [];
                    } else {
                        inputItem.input = "";
                    }
                }
            }
        },
        copyAPIUrl() {
            const inputDom = document.createElement('input');
            document.body.appendChild(inputDom);
            inputDom.setAttribute('value', "http://192.168.121.127:6869/api/" + this.info.table + "/" + this.param.id);
            inputDom.select();
            document.execCommand("copy"); // 执行浏览器复制命令
            if (document.execCommand('copy')) {
                document.execCommand('copy');
            }
            document.body.removeChild(inputDom);
        },
        addGoods() {
            console.log("执行了吗？");
            this.input.回购礼.商品信息.push({
                名称: "", 总价格: "", 总容量: "", SKU类型: "", SKU品类: "", 套装件数: ""
            });
        },
        removeGoods(event) {
            const target = event.target,
                idx = target.dataset.index;

            this.input.回购礼.商品信息.splice(idx, 1);
        },
        request(type) {
            let _this = this;
            if (type === "get_data") {
                $.ajax({
                    method: "GET",
                    url: "http://192.168.121.127:6869/data/get",
                    headers: {
                        "token": sessionStorage.getItem("token")
                    },
                    data: {
                        table: this.info.table,
                        id: this.param.id
                    },
                    success(resp) {
                        if (resp.code === 1) {
                            const dataDict = resp.data.detail.data;
                            for (let i = 0, len = _this.inputList.length; i < len; i++) {
                                const inputItem = _this.inputList[i];
                                inputItem.input = dataDict[inputItem.key];
                            }
                            _this.data = resp.data.detail;
                        }
                    }
                })
            }
            else if (type === "add_data") {
                this.$refs.popup.open("default", "正在添加数据中，请稍等......");
                setTimeout(() => {
                    $.ajax({
                        method: "POST",
                        url: "http://192.168.121.127:6869/data/add",
                        headers: {
                            "Content-Type": "application/json",
                            "token": sessionStorage.getItem("token")
                        },
                        dataType: "JSON",
                        data: JSON.stringify({
                            table: this.info.table,
                            data: this.getInputData()
                        }),
                        success(resp) {
                            if (resp.code === 1) {
                                _this.$refs.popup.setAll("success", resp.msg);
                                setTimeout(() => {
                                    _this.$refs.popup.close();
                                    if (_this.other.addStatus === 0) {
                                        _this.$router.back();
                                    } else if (_this.other.addStatus === 1) {
                                        _this.$router.push("detail?type=edit&title=" + _this.title + "&id=" + resp.data.id);
                                    }
                                }, 2000);
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
            else if (type === "update_data") {
                this.$refs.popup.open("default", "正在保存数据中，请稍等......");
                setTimeout(() => {
                    $.ajax({
                        method: "POST",
                        url: "http://192.168.121.127:6869/data/update",
                        headers: {
                            "Content-Type": "application/json",
                            "token": sessionStorage.getItem("token")
                        },
                        dataType: "JSON",
                        data: JSON.stringify({
                            table: this.info.table,
                            id: this.param.id,
                            data: this.getInputData()
                        }),
                        success(resp) {
                            if (resp.code === 1) {
                                _this.$refs.popup.setAll("success", resp.msg);
                                setTimeout(() => {
                                    _this.$refs.popup.close();
                                }, 2000);
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
            else if (type === "copy_data") {
                $("#modalCopy").modal("hide");
                this.$refs.popup.open("default", "正在复制数据中，请稍等......");
                setTimeout(() => {
                    $.ajax({
                        method: "POST",
                        url: "http://192.168.121.127:6869/data/copy",
                        headers: {
                            "Content-Type": "application/json",
                            "token": sessionStorage.getItem("token")
                        },
                        dataType: "JSON",
                        data: JSON.stringify({
                            table: this.info.table,
                            id: this.param.id
                        }),
                        success(resp) {
                            if (resp.code === 1) {
                                _this.$refs.popup.setAll("success", resp.msg);
                                setTimeout(() => {
                                    _this.$refs.popup.close();
                                    if (_this.other.copyAndSkip === 1) {
                                        _this.$router.push("detail?type=edit&title=" + _this.title + "&id=" + resp.data.id);
                                    }
                                }, 2000);
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
            else if (type === "delete_data") {
                $("#modalDelete").modal("hide");
                this.$refs.popup.open("default", "正在删除数据中，请稍等......");
                setTimeout(() => {
                    $.ajax({
                        method: "POST",
                        url: "http://192.168.121.127:6869/data/delete",
                        headers: {
                            "Content-Type": "application/json",
                            "token": sessionStorage.getItem("token")
                        },
                        dataType: "JSON",
                        data: JSON.stringify({
                            table: this.info.table,
                            id: this.param.id
                        }),
                        success(resp) {
                            if (resp.code === 1) {
                                _this.$refs.popup.setAll("success", resp.msg);
                                setTimeout(() => {
                                    _this.$refs.popup.close();
                                    _this.$router.back();
                                }, 3000);
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
        },
        getInputData() {
            let inputData = {};
            for (let i = 0, len = this.inputList.length; i < len; i++) {
                const inputItem = this.inputList[i];
                inputData[inputItem.key] = inputItem.input;
            }
            return inputData;
        },
        openPopup(type) {
            if (type === "delete") {
                $("#modalDelete").modal({
                    backdrop: "static"
                });
            } else if (type === "copy") {
                $("#modalCopy").modal({
                    backdrop: "static"
                });
            }
        }
    }
}
</script>

<style lang="scss" scoped>
.payload-detail {
    .payload-detail-header {
        padding: 0 10px 10px;
        border-bottom: 2px dashed rgba(0, 0, 0, 0.1);
    }

    .payload-detail-body {
        margin-top: 20px;

        .input-area {
            height: 100%;
            border-right: 1px solid rgba(0, 0, 0, 0.1);
            padding-bottom: 20px;
            overflow: auto;

            .input-group-custom {
                .input-group-header {
                    display: flex;
                    flex-direction: row;
                    justify-content: space-between;
                    width: 100%;
                    height: 40px;
                    line-height: 40px;
                    margin-bottom: 10px;
                    border-bottom: 1px solid rgba(0, 0, 0, 0.1);

                    .input-op-area {
                        width: 50px;

                        i {
                            font-size: 16px;
                            font-weight: bold;
                            cursor: pointer;
                        }
                    }
                }

                .form-goods {
                    border-radius: 10px;
                    border: 1px solid rgba(0, 0, 0, 0.1);
                    margin-top: 10px;
                    padding: 10px;
                    // box-shadow: 2px 3px 3px 2px rgba(0, 0, 0, 0.5);

                    .form-goods-header {
                        height: 30px;
                        line-height: 30px;
                        text-align: right;

                        i {
                            font-size: 16px;
                            margin-right: 10px;
                            cursor: pointer;
                        }
                    }
                }

                .table-op-area {
                    width: 100%;
                    margin-top: 10px;
                    text-align: center;

                    i {
                        width: 100px;
                    }
                }

                .unseen {
                    visibility: hidden;
                }
            }
        }

        .input-area::-webkit-scrollbar {
            width: 4px;
        }

        .input-area::-webkit-scrollbar-thumb {
            border-radius: 10px;
            box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.2);
            background: rgba(0, 0, 0, 0.2);
        }

        .input-area::-webkit-scrollbar-track {
            box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.2);
            border-radius: 0;
            background: rgba(0, 0, 0, 0.1);
        }

        .info-area {
            position: relative;
            height: 100%;
            padding: 10px 30px;

            .info-op-area {
                width: 100%;
                height: 50px;
            }

            .info-list {
                position: absolute;
                bottom: 20px;
                left: 30px;
                width: 90%;
                height: 200px;

                .info-item {
                    width: 100%;
                    height: 60px;
                    margin-top: 10px;

                    .info-item-name {
                        color: #aaa;
                        font-size: 16px;

                        // font-weight: bold;
                        .icon-url-copy {
                            cursor: pointer;
                        }
                    }

                    .info-item-value {
                        // width: 80%;
                        margin-top: 10px;
                        overflow: hidden;
                        text-overflow: ellipsis;
                        white-space: nowrap;

                        a {
                            width: 100%;
                        }
                    }
                }
            }
        }
    }
}
</style>