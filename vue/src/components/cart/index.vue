<template>
    <TransitionRoot as="template" :show="cartIsShow" class="z-50">
        <div class="fixed inset-0 overflow-hidden">
            <div class="absolute inset-0 overflow-hidden">
                <TransitionChild as="template" enter="ease-in-out duration-500" enter-from="opacity-0"
                    enter-to="opacity-100" leave="ease-in-out duration-500" leave-from="opacity-100"
                    leave-to="opacity-0">
                    <div class="absolute inset-0 bg-gray-500 bg-opacity-75 transition-opacity" @click="cartIsNotShow" />
                </TransitionChild>
                <div class="fixed inset-y-0 right-0 pl-10 max-w-full flex">
                    <TransitionChild as="template" enter="transform transition ease-in-out duration-500 sm:duration-700"
                        enter-from="translate-x-full" enter-to="translate-x-0"
                        leave="transform transition ease-in-out duration-500 sm:duration-700" leave-from="translate-x-0"
                        leave-to="translate-x-full">
                        <div class="relative w-screen max-w-md">
                            <TransitionChild as="template" enter="ease-in-out duration-500" enter-from="opacity-0"
                                enter-to="opacity-100" leave="ease-in-out duration-500" leave-from="opacity-100"
                                leave-to="opacity-0">
                                <div class="absolute top-0 left-0 -ml-8 pt-4 pr-2 flex sm:-ml-10 sm:pr-4">
                                    <button type="button"
                                        class="rounded-md text-gray-300 hover:text-white focus:outline-none focus:ring-2 focus:ring-white"
                                        @click="cartIsNotShow">
                                        <span class="sr-only">Close panel</span>
                                        <XIcon class="h-6 w-6" aria-hidden="true" />
                                    </button>
                                </div>
                            </TransitionChild>

                            <!-- start -->
                            <div class="h-full flex flex-col py-6 bg-white shadow-xl overflow-y-scroll">
                                <div class="px-4 sm:px-6">
                                    <div class="text-4xl font-Shippori text-gray-900 border-b-2 border-gray-200 pb-4">
                                        ご注文内容
                                    </div>
                                </div>
                                <div class="mt-6 relative flex-1 px-4 sm:px-6">

                                    <div id="orderBox" v-if="!payViewIsShow"
                                        class="flex flex-col justify-between h-full">
                                        <ul class="flex-grow max-h-70vh overflow-y-scroll">
                                            <li v-for="(item,index) in orderList" :key="item.item+index"
                                                class="flex justify-between pb-2 mb-2 border-b border-gray-300">
                                                <div class="w-1/3">
                                                    <img :src=item.item.imgSrc alt="">
                                                </div>
                                                <div class="w-2/3 pl-4 flex flex-col">
                                                    <div class="flex mb-1">
                                                        <h2 class="mr-4">{{item.item.name}}</h2>
                                                        <p>X{{item.count}}</p>
                                                    </div>
                                                    <div>
                                                        <p>¥{{item.total}}</p>
                                                    </div>
                                                    <div class="flex-grow relative">
                                                        <button
                                                            class="absolute bottom-0 right-1 text-gray-400 hover:text-gray-500 underline"
                                                            @click='deleteOrder(index)'>削除</button>
                                                    </div>
                                                </div>
                                            </li>
                                        </ul>
                                        <div class="buttomBox flex-1 flex flex-col justify-end mb-2">
                                            <p class="text-xl font-Shippori">合計 : ¥{{cartTotal}}</p>
                                        </div>
                                        <div class="flex justify-center items-center" v-if="!payViewIsShow">
                                            <button @click="toPay" :class="[classObj.toPayBtn.grey ? 'bg-gray-500' : 'bg-red-500 hover:bg-red-600']"
                                                class=" text-white px-6 sm:px-12 py-2 sm:py-4 rounded-full">お会計に進む</button>
                                        </div>
                                    </div>

                                    <div id="payBox" v-if="payViewIsShow" class="flex flex-col justify-between h-full">
                                        <ul class="flex-grow max-h-40vh overflow-y-scroll">
                                            <li v-for="(item,index) in orderList" :key="item.item+index"
                                                class="flex justify-between items-center pb-2 mb-2 border-b border-gray-300">
                                                <div class="w-1/6">
                                                    <img :src=item.item.imgSrc alt="">
                                                </div>
                                                <div class="flex flex-grow justify-end">
                                                    <h2 class="mr-4">{{item.item.name}}</h2>
                                                    <p>X{{item.count}}</p>
                                                </div>
                                                <div class="w-1/4 flex justify-end">
                                                    <p>¥{{item.total}}</p>
                                                </div>
                                            </li>
                                        </ul>
                                        <div id="addressList" class="mt-6 flex-1">
                                            <p
                                                class="text-4xl font-Shippori text-gray-900 border-b-2 border-gray-200 pb-4">
                                                お届け先</p>
                                            <ul v-if="isShow_addressList">
                                                <li v-for="(item,index) in userAddressList" :key="item+index"
                                                    :class="[index==isActive ? 'bg-gray-300':'','my-2 p-2 cursor-pointer']" @click="checkAddress(index)">
                                                    <p>{{"〒" + item.postCode}}<span
                                                            v-if="index==isActive" class="text-red-500">&nbsp;&nbsp;&nbsp;&nbsp;✓</span>
                                                    </p>
                                                    <p>{{item.prefecture + item.municipality + item.address + ' ' + item.building}}
                                                    </p>
                                                </li>
                                            </ul>
                                            <p v-if="!isShow_addressList" id="address_add_btn"
                                                class="flex justify-center mt-2 text-indigo-600 hover:text-indigo-500 cursor-pointer"
                                                @click="toMinePage">
                                                +お届け先を追加する
                                            </p>
                                        </div>
                                        <div class="buttomBox flex-1 flex flex-col justify-end mb-2">
                                            <p class="text-xl font-Shippori">合計 : ¥{{cartTotal}}</p>
                                        </div>
                                        <div class="flex justify-center items-center" v-if="payViewIsShow">
                                            <button @click="back"
                                                class="bg-gray-500 hover:bg-gray-600 text-white px-6 sm:px-12 py-2 sm:py-4 rounded-full mr-4">前のページ</button>
                                            <button @click="pay"
                                                class=" text-white px-6 sm:px-12 py-2 sm:py-4 rounded-full"
                                                :class="[!isShow_addressList ? 'bg-gray-500' :'bg-red-500 hover:bg-red-600']">注文する</button>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <!-- end -->
                        </div>
                    </TransitionChild>
                </div>
            </div>
        </div>
    </TransitionRoot>
</template>

<script>
    import {
        TransitionChild,
        TransitionRoot
    } from '@headlessui/vue'
    import {
        XIcon
    } from '@heroicons/vue/outline'


    import {
        PostRequest
    } from '@/apis/read.js'

    export default {
        name: 'Cart',

        components: {
            TransitionChild,
            TransitionRoot,
            XIcon,
        },

        data() {
            return {
                cartTotal: 0,
                classObj: {
                    toPayBtn: {
                        grey: true,
                    }
                },
            }
        },

        computed: {
            userAddressList() {
                return this.$store.state.userStore.userData.userAddressList
            },
            isShow_addressList() {
                if (this.userAddressList.length > 0) {
                    return true
                }
                return false
            },
            isActive() {
                return this.$store.state.cartList.isActive
            },
            userAddress() {
                return this.$store.state.userStore.userData.userAddressList[this.$store.state.cartList.isActive]
            },
            orderList() {
                return this.$store.state.cartList.Value
            },
            payViewIsShow() {
                return this.$store.state.cartList.payView
            },
            cartIsShow() {
                return this.$store.state.cartShow.Value
            }
        },

        methods: {
            deleteOrder(index) {
                this.orderList.splice(index, 1);
            },
            toPay() {
                if (this.orderList.length <= 0) return
                if (!this.$store.state.userStore.isLogined) {
                    alert("ログインしてください");
                    this.cartIsNotShow();
                    this.$router.push('/login');
                    return
                }
                this.$store.commit('cartList/PAYVIEW', true);
            },
            back() {
                this.$store.commit('cartList/PAYVIEW', false);
            },
            checkAddress(index) {
                this.$store.commit('cartList/ISACTIVE', index);
            },
            toMinePage() {
                this.$router.push('/mine/' + this.$store.state.userStore.userID);
                this.cartIsNotShow();
            },
            pay() {
                if (!this.isShow_addressList) {
                    alert("お届け先を選んでください")
                    return
                }
                const params = {
                    url: '/add_order',
                    key: this.$store.state.userStore.userID,
                    data: {
                        id: 1,
                        orderList: this.orderList,
                        userAddress: this.userAddress,
                        cartTotal: this.cartTotal
                    }
                };
                PostRequest(params).then(response => {
                    return response
                });
                alert("ご注文を受付けました！")
                this.cartIsNotShow();
                this.$store.commit('cartList/CARTLIST', []);
                this.$store.commit('cartList/PAYVIEW', false);
                this.$router.push('/');
            },
            cartIsNotShow() {
                this.$store.commit('cartShow/CARTSHOW', false);
                this.Move();
                this.back();
            },
            Move() {
                document.body.style.overflow = ''; //出现滚动条
            }
        },

        watch: {
            orderList: {
                handler() {
                    this.cartTotal = 0;
                    for (let i = 0; i < this.orderList.length; i++) {
                        this.cartTotal += this.orderList[i].total;
                    }
                    if (this.orderList.length > 0) {
                        this.classObj.toPayBtn.grey = false;
                    } else {
                        this.classObj.toPayBtn.grey = true;
                    }
                },
                immediate: true,
                deep: true,
            },
        },
    }
</script>