<template>
    <div class="payload-detail">

        <div class="payload-detail-header">
            <h3 v-if="param.type === 'add'"><b>话术模板</b></h3>
            <h3 v-else-if="param.type === 'edit'">
                <b>话术模板：</b>
                <span v-text="input.标题"></span>
            </h3>
        </div>

        <div class="payload-detail-body">

            <div id="inputRow" class="row mt-20">
                <div id="inputArea" class="col-md-8 input-area">
                    <form>
                        <div class="form-group">
                            <label class="control-label">
                                <span class="color-red">★</span>
                                模板数据名称：
                            </label>
                            <input v-model="input.标题" type="text" class="form-control" />
                            <p class="help-block">当前话术模板数据的名称，用于在列表中进行检索和管理，请输入 24 字以内的中文~</p>
                        </div>
                    </form>
                    <form class="form-inline">
                        <div class="form-group module-select">
                            <label class="control-label mr-20">
                                <span class="color-red mr-5">★</span>填写模块选择：
                            </label>
                            <div class="module-block">
                                <label class="checkbox-inline">
                                    <input v-model="setting.select" type="checkbox" id="inlineCheckbox1" value="外呼任务"> 外呼任务
                                </label>
                                <label class="checkbox-inline">
                                    <input v-model="setting.select" type="checkbox" id="inlineCheckbox1" value="客户"> 客户
                                </label>
                                <label class="checkbox-inline">
                                    <input v-model="setting.select" type="checkbox" id="inlineCheckbox2" value="品牌"> 品牌
                                </label>
                                <label class="checkbox-inline">
                                    <input v-model="setting.select" type="checkbox" id="inlineCheckbox3" value="店铺"> 店铺
                                </label>
                                <label class="checkbox-inline">
                                    <input v-model="setting.select" type="checkbox" id="inlineCheckbox3" value="链接"> 链接
                                </label>
                                <label class="checkbox-inline">
                                    <input v-model="setting.select" type="checkbox" id="inlineCheckbox3" value="小程序"> 小程序
                                </label>
                                <label class="checkbox-inline">
                                    <input v-model="setting.select" type="checkbox" id="inlineCheckbox3" value="活动"> 活动
                                </label>
                                <label class="checkbox-inline">
                                    <input v-model="setting.select" type="checkbox" id="inlineCheckbox3" value="回购礼"> 回购礼
                                </label>
                                <label class="checkbox-inline">
                                    <input v-model="setting.select" type="checkbox" id="inlineCheckbox3" value="买赠"> 买赠
                                </label>
                                <label class="checkbox-inline">
                                    <input v-model="setting.select" type="checkbox" id="inlineCheckbox3" value="积分礼"> 积分礼
                                </label>
                                <label class="checkbox-inline">
                                    <input v-model="setting.select" type="checkbox" id="inlineCheckbox3" value="满赠"> 满赠
                                </label>
                                <label class="checkbox-inline">
                                    <input v-model="setting.select" type="checkbox" id="inlineCheckbox3" value="购后抽奖"> 购后抽奖
                                </label>
                                <label class="checkbox-inline">
                                    <input v-model="setting.select" type="checkbox" id="inlineCheckbox3" value="优惠券"> 优惠券
                                </label>
                            </div>
                        </div>
                    </form>
                    <form class="form mt-20">
                        <div v-if="setting.select.indexOf('外呼任务') + 1" class="input-group-custom">
                            <div class="input-group-header">
                                <h4 class="input-title">外呼任务</h4>
                                <div class="input-op-area">
                                    <!-- <i class="glyphicon glyphicon-refresh mr-10" data-toggle="tooltip"
                                            data-placement="top" title="清空"></i> -->
                                    <i v-if="setting.fold[5]" @click="setting.fold[5] = !setting.fold[5];"
                                        class="glyphicon glyphicon-chevron-up"></i>
                                    <i v-else @click="setting.fold[5] = !setting.fold[5];"
                                        class="glyphicon glyphicon-chevron-down"></i>
                                </div>
                            </div>
                            <div v-if="setting.fold[5]" class="pt-10">
                                <div class="form-group">
                                    <label class="control-label">
                                        <span>标签</span>
                                    </label>
                                    <div class="pl-10">
                                        <div class="checkbox">
                                            <label class="mr-10">
                                                <input v-model="input.外呼任务.标签" type="checkbox" value="一周内">
                                                <span>发短信</span>
                                            </label>
                                            <label class="mr-10">
                                                <input v-model="input.外呼任务.标签" type="checkbox" value="一个月内">
                                                <span>挽回</span>
                                            </label>
                                            <label class="mr-10">
                                                <input v-model="input.外呼任务.标签" type="checkbox" value="三个月内">
                                                <span>预售</span>
                                            </label>
                                            <label class="mr-10">
                                                <input v-model="input.外呼任务.标签" type="checkbox" value="一年内">
                                                <span>尾款</span>
                                            </label>
                                            <label class="mr-10">
                                                <input v-model="input.外呼任务.标签" type="checkbox" value="一年前">
                                                <span>短信已发送</span>
                                            </label>
                                            <label class="mr-10">
                                                <input v-model="input.外呼任务.标签" type="checkbox" value="无">
                                                <span>活动通知</span>
                                            </label>
                                            <label class="mr-10">
                                                <input v-model="input.外呼任务.标签" type="checkbox" value="无">
                                                <span>私域加微</span>
                                            </label>
                                        </div>
                                    </div>
                                </div>
                                <div class="form-group">
                                    <label class="control-label">
                                        <span>外呼时间</span>
                                    </label>
                                    <input v-model="input.外呼任务.外呼时间" type="datetime-local" class="form-control" />
                                </div>
                                <div class="form-group">
                                    <label class="control-label">
                                        <span>定金开始时间</span>
                                    </label>
                                    <input v-model="input.外呼任务.定金开始时间" type="datetime-local" class="form-control" />
                                </div>
                                <div class="form-group">
                                    <label class="control-label">
                                        <span>定金截止时间</span>
                                    </label>
                                    <input v-model="input.外呼任务.定金截止时间" type="datetime-local" class="form-control" />
                                </div>
                                <div class="form-group">
                                    <label class="control-label">
                                        <span>尾款开始时间</span>
                                    </label>
                                    <input v-model="input.外呼任务.尾款开始时间" type="datetime-local" class="form-control" />
                                </div>
                                <div class="form-group">
                                    <label class="control-label">
                                        <span>尾款截止时间</span>
                                    </label>
                                    <input v-model="input.外呼任务.尾款截止时间" type="datetime-local" class="form-control" />
                                </div>
                            </div>
                        </div>
                        <div v-if="setting.select.indexOf('客户') + 1" class="input-group-custom">
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
                            <div v-if="setting.fold[0]" class="pt-10">
                                <div class="form-group">
                                    <label class="control-label">
                                        <span>购买时间</span>
                                    </label>
                                    <div class="pl-10">
                                        <div class="checkbox">
                                            <label class="mr-10">
                                                <input v-model="input.客户.购买时间" type="checkbox" value="一周内">
                                                <span>一周内</span>
                                            </label>
                                            <label class="mr-10">
                                                <input v-model="input.客户.购买时间" type="checkbox" value="一个月内">
                                                <span>一个月内</span>
                                            </label>
                                            <label class="mr-10">
                                                <input v-model="input.客户.购买时间" type="checkbox" value="三个月内">
                                                <span>三个月内</span>
                                            </label>
                                            <label class="mr-10">
                                                <input v-model="input.客户.购买时间" type="checkbox" value="一年内">
                                                <span>一年内</span>
                                            </label>
                                            <label class="mr-10">
                                                <input v-model="input.客户.购买时间" type="checkbox" value="一年前">
                                                <span>一年前</span>
                                            </label>
                                            <label class="mr-10">
                                                <input v-model="input.客户.购买时间" type="checkbox" value="无">
                                                <span>无</span>
                                            </label>
                                        </div>
                                    </div>
                                </div>
                                <div class="form-group">
                                    <label class="control-label">
                                        <span>购买商品</span>
                                    </label>
                                    <input v-model="input.客户.购买商品" type="text" class="form-control" />
                                </div>
                                <div class="form-group">
                                    <label class="control-label">
                                        <span>客户类型</span>
                                    </label>
                                    <div class="pl-10 mt-10">
                                        <label class="radio-inline">
                                            <input type="radio" v-model="input.客户.客户类型" name="客户类型" value="老会员">
                                            老会员
                                        </label>
                                        <label class="radio-inline">
                                            <input type="radio" v-model="input.客户.客户类型" name="客户类型" value="新会员">
                                            新会员
                                        </label>
                                        <label class="radio-inline">
                                            <input type="radio" v-model="input.客户.客户类型" name="客户类型" value="">
                                            无
                                        </label>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div v-if="setting.select.indexOf('品牌') + 1" class="input-group-custom">
                            <div class="input-group-header">
                                <h4 class="input-title">品牌</h4>
                                <div class="input-op-area">
                                    <i v-if="setting.fold[1]" @click="setting.fold[1] = !setting.fold[1];"
                                        class="glyphicon glyphicon-chevron-up"></i>
                                    <i v-else @click="setting.fold[1] = !setting.fold[1];"
                                        class="glyphicon glyphicon-chevron-down"></i>
                                </div>
                            </div>
                            <div class="pt-10" v-if="setting.fold[1]">
                                <div class="form-group">
                                    <label class="control-label">名称</label>
                                    <input v-model="input.品牌.名称" type="text" class="form-control" />
                                </div>
                                <div class="form-group">
                                    <label class="control-label">国家</label>
                                    <div class="pl-10 mt-10">
                                        <label class="radio-inline">
                                            <input type="radio" v-model="input.品牌.国家" name="品牌国家" value="法国">
                                            法国
                                        </label>
                                        <label class="radio-inline">
                                            <input type="radio" v-model="input.品牌.国家" name="品牌国家" value="">
                                            无
                                        </label>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div v-if="setting.select.indexOf('店铺') + 1" class="input-group-custom">
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
                            <div v-if="setting.fold[2]" class="pt-10">
                                <div class="form-group">
                                    <label class="control-label">名称</label>
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
                        <div v-if="setting.select.indexOf('链接') + 1" class="input-group-custom">
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
                            <div v-if="setting.fold[3]" class="pt-10">
                                <div class="form-group">
                                    <label class="control-label">类型</label>
                                    <div class="pl-10 mt-10">
                                        <label class="radio-inline">
                                            <input type="radio" v-model="input.链接.类型" name="链接类型" value="店铺">
                                            店铺
                                        </label>
                                        <label class="radio-inline">
                                            <input type="radio" v-model="input.链接.类型" name="链接类型" value="品牌">
                                            品牌
                                        </label>
                                        <label class="radio-inline">
                                            <input type="radio" v-model="input.链接.类型" name="链接类型" value="活动">
                                            活动
                                        </label>
                                        <label class="radio-inline">
                                            <input type="radio" v-model="input.链接.类型" name="链接类型" value="优惠券">
                                            优惠券
                                        </label>
                                        <label class="radio-inline">
                                            <input type="radio" v-model="input.链接.类型" name="链接类型" value="商品">
                                            商品
                                        </label>
                                        <label class="radio-inline">
                                            <input type="radio" v-model="input.链接.类型" name="链接类型" value="">
                                            无
                                        </label>
                                    </div>
                                </div>
                                <div class="form-group">
                                    <label class="control-label">URL</label>
                                    <input v-model="input.链接.url" type="text" class="form-control" />
                                </div>
                            </div>
                        </div>

                        <ul class="nav nav-tabs" role="tablist">
                            <li v-if="setting.select.indexOf('小程序') + 1" role="presentation"><a href="#小程序"
                                    data-toggle="tab">小程序</a></li>
                            <li v-if="setting.select.indexOf('活动') + 1" role="presentation"><a href="#活动"
                                    data-toggle="tab">活动</a></li>
                            <li v-if="setting.select.indexOf('回购礼') + 1" role="presentation"><a href="#回购礼"
                                    data-toggle="tab">回购礼</a></li>
                            <li v-if="setting.select.indexOf('买赠') + 1" role="presentation"><a href="#买赠"
                                    data-toggle="tab">买赠</a></li>
                            <li v-if="setting.select.indexOf('积分礼') + 1" role="presentation"><a href="#积分礼"
                                    data-toggle="tab">积分礼</a></li>
                            <li v-if="setting.select.indexOf('满赠') + 1" role="presentation"><a href="#满赠"
                                    data-toggle="tab">满赠</a></li>
                            <li v-if="setting.select.indexOf('购后抽奖') + 1" role="presentation"><a href="#购后抽奖"
                                    data-toggle="tab">购后抽奖</a></li>
                            <li v-if="setting.select.indexOf('优惠券') + 1" role="presentation"><a href="#优惠券"
                                    data-toggle="tab">优惠券</a></li>
                        </ul>
                        <div v-if="setting.tabShow" class="tab-content mt-20">
                            <div role="tabpanel" class="tab-pane" id="小程序">
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
                                    <div class="form-group border-area">
                                        <label class="control-label">商品信息</label>
                                        <ul class="list-group">
                                            <li class="list-group-item" v-for="(item, idx) in input.回购礼.商品信息" :key="idx">
                                                <div class="list-group-item-value" v-text="item.show"></div>
                                                <div class="list-group-item-ops">
                                                    <i @click="editGoods" class="glyphicon glyphicon-edit mr-10" :data-index="idx" data-group="回购礼" data-param="商品信息"></i>
                                                    <i @click="removeGoods" class="glyphicon glyphicon-trash"
                                                    :data-index="idx" data-group="回购礼" data-param="商品信息"></i>
                                                </div>
                                            </li>
                                        </ul>
                                        <div class="table-op-area">
                                            <div @click="openPopup('addGoods', {group: '回购礼', param: '商品信息'})" class="btn btn-default"
                                                data-group="回购礼" data-param="商品信息">
                                                <i class="glyphicon glyphicon-plus"></i>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="form-group border-area">
                                        <label class="control-label">赠品信息</label>
                                        <ul class="list-group">
                                            <li class="list-group-item" v-for="(item, idx) in input.回购礼.赠品信息" :key="idx">
                                                <div class="list-group-item-value" v-text="item.show"></div>
                                                <div class="list-group-item-ops">
                                                    <i @click="editGoods" class="glyphicon glyphicon-edit mr-10" :data-index="idx" data-group="回购礼" data-param="赠品信息"></i>
                                                    <i @click="removeGoods" class="glyphicon glyphicon-trash"
                                                    :data-index="idx" data-group="回购礼" data-param="赠品信息"></i>
                                                </div>
                                            </li>
                                        </ul>
                                        <div class="table-op-area">
                                            <div @click="openPopup('addGoods', {group: '回购礼', param: '赠品信息'})" class="btn btn-default"
                                                data-group="回购礼" data-param="赠品信息">
                                                <i class="glyphicon glyphicon-plus"></i>
                                            </div>
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
                            <div role="tabpanel" class="tab-pane" id="买赠">
                                <div class="input-group-custom">
                                    <div class="form-group border-area">
                                        <label class="control-label">商品信息</label>
                                        <ul class="list-group">
                                            <li class="list-group-item" v-for="(item, idx) in input.买赠.商品信息" :key="idx">
                                                <div class="list-group-item-value" v-text="item.show"></div>
                                                <div class="list-group-item-ops">
                                                    <i @click="editGoods" class="glyphicon glyphicon-edit mr-10" :data-index="idx" data-group="买赠" data-param="商品信息"></i>
                                                    <i @click="removeGoods" class="glyphicon glyphicon-trash"
                                                    :data-index="idx" data-group="买赠" data-param="商品信息"></i>
                                                </div>
                                            </li>
                                        </ul>
                                        <div class="table-op-area">
                                            <div @click="openPopup('addGoods', {group: '买赠', param: '商品信息'})" class="btn btn-default"
                                                data-group="买赠" data-param="商品信息">
                                                <i class="glyphicon glyphicon-plus"></i>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="form-group border-area">
                                        <label class="control-label">赠品信息</label>
                                        <ul class="list-group">
                                            <li class="list-group-item" v-for="(item, idx) in input.买赠.赠品信息" :key="idx">
                                                <div class="list-group-item-value" v-text="item.show"></div>
                                                <div class="list-group-item-ops">
                                                    <i @click="editGoods" class="glyphicon glyphicon-edit mr-10" :data-index="idx" data-group="买赠" data-param="赠品信息"></i>
                                                    <i @click="removeGoods" class="glyphicon glyphicon-trash"
                                                    :data-index="idx" data-group="买赠" data-param="赠品信息"></i>
                                                </div>
                                            </li>
                                        </ul>
                                        <div class="table-op-area">
                                            <div @click="openPopup('addGoods', {group: '买赠', param: '赠品信息'})" class="btn btn-default"
                                                data-group="买赠" data-param="赠品信息">
                                                <i class="glyphicon glyphicon-plus"></i>
                                            </div>
                                        </div>
                                    </div>

                                    <div class="form-group mt-20">
                                        <label class="control-label">优先级</label>
                                        <select v-model="input.买赠.优先级" class="form-control">
                                            <option value="高">高</option>
                                            <option value="低">低</option>
                                        </select>
                                    </div>
                                    <div class="row">
                                        <div class="form-group col-md-6 col-sm-12">
                                            <label class="control-label">开始日期</label>
                                            <input v-model="input.买赠.开始日期" type="datetime-local" class="form-control" />
                                        </div>
                                        <div class="form-group col-md-6 col-sm-12">
                                            <label class="control-label">截止日期</label>
                                            <input v-model="input.买赠.截止日期" type="datetime-local" class="form-control" />
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label class="control-label">备注信息</label>
                                        <input v-model="input.买赠.备注信息" type="text" class="form-control" />
                                    </div>
                                </div>
                            </div>
                            <div role="tabpanel" class="tab-pane" id="积分礼">
                                <div class="input-group-custom">
                                    <div class="form-group border-area">
                                        <label class="control-label">商品信息</label>
                                        <ul class="list-group">
                                            <li class="list-group-item" v-for="(item, idx) in input.积分礼.商品信息" :key="idx">
                                                <div class="list-group-item-value" v-text="item.show"></div>
                                                <div class="list-group-item-ops">
                                                    <i @click="editGoods" class="glyphicon glyphicon-edit mr-10" :data-index="idx" data-group="积分礼" data-param="商品信息"></i>
                                                    <i @click="removeGoods" class="glyphicon glyphicon-trash"
                                                    :data-index="idx" data-group="积分礼" data-param="商品信息"></i>
                                                </div>
                                            </li>
                                        </ul>
                                        <div class="table-op-area">
                                            <div @click="openPopup('addGoods', {group: '积分礼', param: '商品信息'})" class="btn btn-default"
                                                data-group="积分礼" data-param="商品信息">
                                                <i class="glyphicon glyphicon-plus"></i>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label class="control-label">积分倍率</label>
                                        <input v-model="input.积分礼.积分倍率" type="number" class="form-control" />
                                    </div>
                                    <div class="form-group border-area">
                                        <label class="control-label">兑换品信息</label>
                                        <ul class="list-group">
                                            <li class="list-group-item" v-for="(item, idx) in input.积分礼.兑换品信息" :key="idx">
                                                <div class="list-group-item-value" v-text="item.show"></div>
                                                <div class="list-group-item-ops">
                                                    <i @click="editGoods" class="glyphicon glyphicon-edit mr-10" :data-index="idx" data-group="积分礼" data-param="兑换品信息"></i>
                                                    <i @click="removeGoods" class="glyphicon glyphicon-trash"
                                                    :data-index="idx" data-group="积分礼" data-param="兑换品信息"></i>
                                                </div>
                                            </li>
                                        </ul>
                                        <div class="table-op-area">
                                            <div @click="openPopup('addGoods', {group: '积分礼', param: '兑换品信息'})" class="btn btn-default"
                                                data-group="积分礼" data-param="兑换品信息">
                                                <i class="glyphicon glyphicon-plus"></i>
                                            </div>
                                        </div>
                                    </div>

                                    <div class="form-group mt-20">
                                        <label class="control-label">优先级</label>
                                        <select v-model="input.积分礼.优先级" class="form-control">
                                            <option value="高">高</option>
                                            <option value="低">低</option>
                                        </select>
                                    </div>
                                    <div class="row">
                                        <div class="form-group col-md-6 col-sm-12">
                                            <label class="control-label">开始日期</label>
                                            <input v-model="input.积分礼.开始日期" type="datetime-local"
                                                class="form-control" />
                                        </div>
                                        <div class="form-group col-md-6 col-sm-12">
                                            <label class="control-label">截止日期</label>
                                            <input v-model="input.积分礼.截止日期" type="datetime-local"
                                                class="form-control" />
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label class="control-label">备注信息</label>
                                        <input v-model="input.积分礼.备注信息" type="text" class="form-control" />
                                    </div>
                                </div>
                            </div>
                            <div role="tabpanel" class="tab-pane" id="满赠">
                                <div class="input-group-custom">
                                    <div class="form-group">
                                        <label class="control-label">门槛金额</label>
                                        <input v-model="input.满赠.门槛金额" type="number" class="form-control" />
                                    </div>
                                    <div class="form-group border-area">
                                        <label class="control-label">赠品信息</label>
                                        <ul class="list-group">
                                            <li class="list-group-item" v-for="(item, idx) in input.满赠.赠品信息" :key="idx">
                                                <div class="list-group-item-value" v-text="item.show"></div>
                                                <div class="list-group-item-ops">
                                                    <i @click="editGoods" class="glyphicon glyphicon-edit mr-10" :data-index="idx" data-group="满赠" data-param="赠品信息"></i>
                                                    <i @click="removeGoods" class="glyphicon glyphicon-trash"
                                                    :data-index="idx" data-group="满赠" data-param="赠品信息"></i>
                                                </div>
                                            </li>
                                        </ul>
                                        <div class="table-op-area">
                                            <div @click="openPopup('addGoods', {group: '满赠', param: '赠品信息'})" class="btn btn-default"
                                                data-group="满赠" data-param="赠品信息">
                                                <i class="glyphicon glyphicon-plus"></i>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="form-group mt-20">
                                        <label class="control-label">优先级</label>
                                        <select v-model="input.满赠.优先级" class="form-control">
                                            <option value="高">高</option>
                                            <option value="低">低</option>
                                        </select>
                                    </div>
                                    <div class="row">
                                        <div class="form-group col-md-6 col-sm-12">
                                            <label class="control-label">开始日期</label>
                                            <input v-model="input.满赠.开始日期" type="datetime-local" class="form-control" />
                                        </div>
                                        <div class="form-group col-md-6 col-sm-12">
                                            <label class="control-label">截止日期</label>
                                            <input v-model="input.满赠.截止日期" type="datetime-local" class="form-control" />
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label class="control-label">备注信息</label>
                                        <input v-model="input.满赠.备注信息" type="text" class="form-control" />
                                    </div>
                                </div>
                            </div>
                            <div role="tabpanel" class="tab-pane" id="购后抽奖">
                                <div class="input-group-custom">
                                    <div class="form-group border-area">
                                        <label class="control-label">商品信息</label>
                                        <ul class="list-group">
                                            <li class="list-group-item" v-for="(item, idx) in input.购后抽奖.商品信息" :key="idx">
                                                <div class="list-group-item-value" v-text="item.show"></div>
                                                <div class="list-group-item-ops">
                                                    <i @click="editGoods" class="glyphicon glyphicon-edit mr-10" :data-index="idx" data-group="购后抽奖" data-param="商品信息"></i>
                                                    <i @click="removeGoods" class="glyphicon glyphicon-trash"
                                                    :data-index="idx" data-group="购后抽奖" data-param="商品信息"></i>
                                                </div>
                                            </li>
                                        </ul>
                                        <div class="table-op-area">
                                            <div @click="openPopup('addGoods', {group: '购后抽奖', param: '商品信息'})" class="btn btn-default"
                                                data-group="购后抽奖" data-param="商品信息">
                                                <i class="glyphicon glyphicon-plus"></i>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="form-group border-area">
                                        <label class="control-label">奖项</label>
                                        <div class="form form-goods" v-for="(item, idx) in input.购后抽奖.奖项" :key="idx">
                                            <div class="form-goods-header">
                                                <i @click="removeGoods" class="glyphicon glyphicon-remove"
                                                    :data-index="idx" data-group="购后抽奖" data-param="奖项"></i>
                                            </div>
                                            <div class="row">
                                                <div class="form-group col-md-6 col-sm-12">
                                                    <label class="control-label">等级</label>
                                                    <input v-model="item.等级" type="text" class="form-control" />
                                                </div>
                                                <div class="form-group col-md-6 col-sm-12">
                                                    <label class="control-label">奖金</label>
                                                    <input v-model="item.奖金" type="number" class="form-control" />
                                                </div>    
                                            </div>
                                        </div>
                                        <div class="table-op-area">
                                            <div @click="addGoods" class="btn btn-default"><i
                                                    class="glyphicon glyphicon-plus" data-group="购后抽奖"
                                                    data-param="奖项"></i></div>
                                        </div>
                                    </div>

                                    <div class="row mt-20">
                                        <div class="form-group col-md-2 col-sm-12">
                                            <label class="control-label">
                                                <span class="color-red">★</span>优先级
                                            </label>
                                            <select v-model="input.购后抽奖.优先级" class="form-control">
                                                <option value="高">高</option>
                                                <option value="低">低</option>
                                            </select>
                                        </div>
                                        <div class="form-group col-md-5 col-sm-12">
                                            <label class="control-label">开始日期</label>
                                            <input v-model="input.购后抽奖.开始日期" type="datetime-local"
                                                class="form-control" />
                                        </div>
                                        <div class="form-group col-md-5 col-sm-12">
                                            <label class="control-label">截止日期</label>
                                            <input v-model="input.购后抽奖.截止日期" type="datetime-local"
                                                class="form-control" />
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label class="control-label">备注信息</label>
                                        <input v-model="input.购后抽奖.备注信息" type="text" class="form-control" />
                                    </div>
                                </div>
                            </div>
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
                        <div v-if="param.type === 'add'" @click="request('add_data'); this.other.addStatus = 2;"
                            class="btn btn-default">
                            <i class="glyphicon glyphicon-plus"></i>
                            继续添加
                        </div>
                        <div v-else-if="param.type === 'edit'" @click="request('update_data')" class="btn btn-default">
                            <i class="glyphicon glyphicon-plus"></i>
                            保存
                        </div>
                        <!-- <div v-if="param.type === 'add'" @click="clear" class="btn btn-default">
                            <i class="glyphicon glyphicon-refresh"></i>
                            清空
                        </div> -->
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
                                    :href="'http://localhost:6869/api/template/' + this.param.id" target="_blank"
                                    v-text="'http://localhost:6869/api/template/' + this.param.id"></a>
                            </div>
                        </div>
                        <div class="info-item">
                            <div class="info-item-name">所属用户</div>
                            <div class="info-item-value" v-text="data.user.create"></div>
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

        <!-- 添加商品弹窗 -->
        <div id="modalAddGoods" class="modal fade" role="dialog">
            <div class="modal-dialog modal-lg" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <h4 class="modal-title">商品信息</h4>
                    </div>
                    <div class="modal-body">
                        <div class="form form-goods">
                            <div class="form-group">
                                <label class="control-label">名称</label>
                                <input v-model="goods.input.名称" type="text" class="form-control" />
                            </div>
                            <div class="form-group">
                                <label class="control-label">总价格</label>
                                <input v-model="goods.input.总价格" type="text" class="form-control" />
                                <p class="help-block">单位是 "元", 不用写单位。也可以写成“单价*数量”的格式，如“79*3”，表示 SKU
                                    单价 79 元,
                                    数量为 3 个</p>
                            </div>
                            <div class="form-group">
                                <label class="control-label">总容量</label>
                                <input v-model="goods.input.总容量" type="text" class="form-control" />
                            </div>
                            <div class="row">
                                <div class="form-group col-md-6 col-sm-12">
                                    <label class="control-label">
                                        <span>SKU 类型</span>
                                    </label>
                                    <select v-model="goods.input.SKU类型" class="form-control">
                                        <option value="商品">商品</option>
                                        <option value="套装">套装</option>
                                        <option value="小样">小样</option>
                                        <option value="优惠券">优惠券</option>
                                        <option value="">无</option>
                                    </select>
                                </div>
                                <div class="form-group col-md-6 col-sm-12">
                                    <label class="control-label">SKU 品类</label>
                                    <select v-model="goods.input.SKU品类" class="form-control">
                                        <option value="化妆品">化妆品</option>
                                        <option value="零食">零食</option>
                                        <option value="卫衣">卫衣</option>
                                        <option value="牛仔裤">牛仔裤</option>
                                        <option value="N/A">N/A</option>
                                        <option value="">无</option>
                                    </select>
                                </div>
                            </div>
                            <div v-if="goods.input.SKU类型 === '套装'" class="form-group">
                                <label class="control-label">套装件数</label>
                                <input v-model="goods.input.套装件数" type="number" class="form-control" />
                            </div>
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-default" data-dismiss="modal">
                            <i class="glyphicon glyphicon-remove mr-5"></i>关闭
                        </button>
                        <button v-if="goods.type === 'add'" @click="addGoodsV2" type="button" class="btn btn-default">
                            <i class="glyphicon glyphicon-plus mr-5"></i>添加
                        </button>
                        <button v-else-if="goods.type === 'edit'" @click="finishEdit" type="button" class="btn btn-default">
                            <i class="glyphicon glyphicon-plus mr-5"></i>编辑
                        </button>
                    </div>
                </div>
            </div>
        </div>

        <!-- 添加数据弹窗 -->
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
                date: {},
                user: {}
            },
            configType: "",
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
                标题: "",
                外呼任务: { 标签: [], 外呼时间: "", 定金开始时间: "", 定金截止时间: "", 尾款开始时间: "", 尾款截止时间: "" },
                客户: { 购买时间: [], 购买商品: "", 客户类型: "" },
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
                select: [],
                fold: [true, true, true, true, true, true],
                tabShow: false
            },
            goods: {
                input: {},
                group: "",
                param: "",
                index: 0,
                type: "add"
            }
        }
    },
    watch: {
        "setting.select"() {
            for (let key in this.input) {
                if (!(this.setting.select.indexOf(key) + 1)) {
                    switch (key) {
                        case "外呼任务": {
                            this.input.外呼任务 = { 标签: [], 外呼时间: "", 定金开始时间: "", 定金截止时间: "", 尾款开始时间: "", 尾款截止时间: "" };
                            break;
                        }
                        case "客户": {
                            this.input.客户 = { 购买时间: [], 购买商品: "", 客户类型: "" };
                            break;
                        }
                        case "品牌": {
                            this.input.品牌 = { 名称: "", 国家: "" };
                            break;
                        }
                        case "店铺": {
                            this.input.店铺 = { 名称: "", 平台: [] };
                            break;
                        }
                        case "链接": {
                            this.input.链接 = { 类型: "", url: "" };
                            break;
                        }
                        case "小程序": {
                            this.input.小程序 = { 类型: "", 关键词: "", url: "" };
                            break;
                        }
                        case "活动": {
                            this.input.活动 = { 名称: "", 简称: "", 开始日期: "", 结束日期: "" };
                            break;
                        }
                        case "回购礼": {
                            this.input.回购礼 = { 商品信息: [], 赠品信息: [], 优先级: "高", 开始日期: "", 结束日期: "", 备注信息: "" };
                            break;
                        }
                        case "买赠": {
                            this.input.买赠 = { 商品信息: [], 赠品信息: [], 优先级: "高", 开始日期: "", 结束日期: "", 备注信息: "" };
                            break;
                        }
                        case "积分礼": {
                            this.input.积分礼 = { 商品信息: [], 积分倍率: "", 兑换品信息: [], 优先级: "高", 开始日期: "", 结束日期: "", 备注信息: "" };
                            break;
                        }
                        case "满赠": {
                            this.input.满赠 = { 门槛金额: "", 赠品信息: [], 优先级: "高", 开始日期: "", 结束日期: "", 备注信息: "" };
                            break;
                        }
                        case "购后抽奖": {
                            this.input.购后抽奖 = { 商品信息: [], 奖项: [], 优先级: "高", 开始日期: "", 结束日期: "", 备注信息: "" };
                            break;
                        }
                        case "优惠券": {
                            this.input.优惠券 = { 门槛金额: "", 减免: "", 优先级: "高", 开始日期: "", 结束日期: "", 备注信息: "" };
                            break;
                        }
                    }
                }
            }

            const tabList = ["小程序", "活动", "回购礼", "买赠", "积分礼", "满赠", "购后抽奖", "优惠券"]
            for (let idx in tabList) {
                if (this.setting.select.indexOf(tabList[idx]) + 1) {
                    this.setting.tabShow = true;
                    return;
                }
            }
            this.setting.tabShow = false;
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

            if (_this.param.type === "edit") {
                _this.request("get_data");
            }
        });
    },
    methods: {
        setHeight() {
            let height = document.documentElement.clientHeight;
            document.getElementById("app").style.height = (height - 1) + "px";
            $("#inputRow").height(height - 191);
            $("#inputArea").height(height - 191);
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
        addGoods(event) {
            const target = event.target,
                group = target.dataset.group,
                param = target.dataset.param;

            if (group === "回购礼" && param === "商品信息") {
                this.input.回购礼.商品信息.push({
                    名称: "", 总价格: "", 总容量: "", SKU类型: "", SKU品类: "", 套装件数: ""
                });
            } else if (group === "回购礼" && param === "赠品信息") {
                this.input.回购礼.赠品信息.push({
                    名称: "", 总价格: "", 总容量: "", SKU类型: "", SKU品类: "", 套装件数: ""
                });
            } else if (group === "买赠" && param === "商品信息") {
                this.input.买赠.商品信息.push({
                    名称: "", 总价格: "", 总容量: "", SKU类型: "", SKU品类: "", 套装件数: ""
                });
            } else if (group === "买赠" && param === "赠品信息") {
                this.input.买赠.赠品信息.push({
                    名称: "", 总价格: "", 总容量: "", SKU类型: "", SKU品类: "", 套装件数: ""
                });
            } else if (group === "积分礼" && param === "商品信息") {
                this.input.积分礼.商品信息.push({
                    名称: "", 总价格: "", 总容量: "", SKU类型: "", SKU品类: "", 套装件数: ""
                });
            } else if (group === "积分礼" && param === "兑换品信息") {
                this.input.积分礼.兑换品信息.push({
                    名称: "", 总价格: "", 总容量: "", SKU类型: "", SKU品类: "", 套装件数: ""
                });
            } else if (group === "满赠" && param === "赠品信息") {
                this.input.满赠.赠品信息.push({
                    名称: "", 总价格: "", 总容量: "", SKU类型: "", SKU品类: "", 套装件数: ""
                });
            } else if (group === "购后抽奖" && param === "商品信息") {
                this.input.购后抽奖.商品信息.push({
                    名称: "", 总价格: "", 总容量: "", SKU类型: "", SKU品类: "", 套装件数: ""
                });
            } else if (group === "购后抽奖" && param === "奖项") {
                this.input.购后抽奖.奖项.push({
                    等级: "", 奖金: ""
                });
            }
        },
        addGoodsV2() {
            const group = this.goods.group,
                param = this.goods.param;

            this.goods.type = "add";
            if (param === "商品信息" || param === "赠品信息" || param === "兑换品信息") {
                this.input[group][param].push({
                    ...this.goods.input, 
                    show: Object.values(this.goods.input).filter((a) => {if (a) {return a;}}).join("/")
                });
            } else if (param === "奖项") {
                this.input[group][param].push({
                    等级: "", 奖金: ""
                });
            }
            $("#modalAddGoods").modal("hide");
            this.goods.input = {};
        },
        editGoods(event) {
            const target = event.target,
                idx = target.dataset.index,
                group = target.dataset.group,
                param = target.dataset.param;

            this.goods.type = "edit";
            this.goods.group = group;
            this.goods.param = param;
            this.goods.index = idx;
            $("#modalAddGoods").modal({
                backdrop: "static"
            });
            this.goods.input = this.input[group][param][idx];
        },
        finishEdit() {
            const group = this.goods.group,
                param = this.goods.param,
                index = this.goods.index;

            this.goods.input.show = "";  // 清空 show 字段的内容，避免影响下一次生成的结果
            this.input[group][param][index] = {
                ...this.goods.input, 
                show: Object.values(this.goods.input).filter((a) => {if (a) {return a;}}).join("/")
            };
            $("#modalAddGoods").modal("hide");
            this.goods.input = {};
        },
        removeGoods(event) {
            const target = event.target,
                idx = target.dataset.index,
                group = target.dataset.group,
                param = target.dataset.param;

            this.input[group][param].splice(idx, 1);
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
                        table: "template",
                        id: this.param.id
                    },
                    success(resp) {
                        if (resp.code === 1) {
                            const dataDict = resp.data.detail.data;
                            _this.setting.select = ["外呼任务", "客户", "品牌", "店铺", "链接", "小程序", "活动", "回购礼", "买赠", "积分礼", "满赠", "购后抽奖", "优惠券"];

                            for (let group in dataDict) {
                                for (let param in dataDict[group]) {
                                    if (param === "商品信息" || param === "赠品信息" || param === "兑换品信息") {
                                        dataDict[group][param].show = Object.values(dataDict[group][param]).filter((a) => {if (a) {return a;}}).join("/");
                                    }
                                }
                            }
                            _this.input = dataDict;
                            _this.data.date = resp.data.detail.date;
                            _this.data.user = resp.data.detail.user;
                            _this.setting.select = resp.data.detail.config.select;
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
                            table: "template",
                            data: this.input,
                            config: {
                                select: this.setting.select
                            }
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
                            table: "template",
                            id: this.param.id,
                            data: this.input,
                            config: {
                                select: this.setting.select
                            }
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
        openPopup(type, data) {
            if (type === "delete") {
                $("#modalDelete").modal({
                    backdrop: "static"
                });
            } else if (type === "copy") {
                $("#modalCopy").modal({
                    backdrop: "static"
                });
            } else if (type === "addGoods") {
                $("#modalAddGoods").modal({
                    backdrop: "static"
                });
                this.goods.group = data.group;
                this.goods.param = data.param;
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

            .module-select {

                .module-block {
                    display: flex;
                    flex-direction: row;
                    flex-wrap: wrap;
                    justify-content: flex-start;
                    margin-left: 10px;

                    .checkbox-inline {
                        margin: 10px 10px 0 0;
                    }
                }
            }

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

                .list-group {

                    .list-group-item {
                        display: flex;
                        flex-direction: row;
                        justify-content: space-between;

                        .list-group-item-value {
                            width: 90%;
                            border-right: 2px dashed rgba(0, 0, 0, 0.1);
                        }

                        .list-group-item-ops {
                            display: flex;
                            flex-direction: row;
                            justify-content: center;
                            width: 10%;

                            i {
                                cursor: pointer;
                            }
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

                .border-area {
                    padding: 10px;
                    border-radius: 10px;
                    border: 2px dashed rgba(0, 0, 0, 0.3);
                }
            }

            .help-block {
                margin-top: 10px;
                padding-left: 5px;
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
                height: 260px;

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