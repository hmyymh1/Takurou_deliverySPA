<template lang="">
    <div id="menu" class="relative min-h-screen w-screen">
        <header class="sticky top-0 z-40">
            <Nav />
        </header>

        <div id="menuList" class="bg-gray-100 mt-20">
            <div class="max-w-2xl mx-auto py-16 px-4 sm:py-24 sm:px-6 lg:max-w-7xl lg:px-8">
                <h2 class="text-2xl font-Shippori font-extrabold tracking-tight text-gray-900">お粥&nbsp;&nbsp;一覧</h2>

                <div class="mt-6 grid grid-cols-1 gap-y-10 gap-x-6 sm:grid-cols-2 lg:grid-cols-4 xl:gap-x-8">
                    <div v-for="(item,index) in lists" :key="item+index" class="group relative">
                        <div
                            class="w-full min-h-80 bg-gray-200 aspect-w-1 aspect-h-1 rounded-md overflow-hidden group-hover:opacity-75 lg:h-80 lg:aspect-none">
                            <img :src="item.imgSrc"
                                class="w-full h-full object-center object-cover lg:w-full lg:h-full" />
                        </div>
                        <div class="my-4 flex justify-between">
                            <div>
                                <h3 class="text-xl text-gray-700 font-Yuji">
                                    <p>
                                        <span aria-hidden="true" class="absolute inset-0" />
                                        {{ item.name }}
                                    </p>
                                </h3>
                                <p class="mt-1 text-sm font-Shippori text-gray-500">{{ item.description }}</p>
                            </div>
                            <p class="text-xl font-Shippori text-gray-900">¥{{ item.price }}</p>
                        </div>
                        <button @click=order(item)
                            class="absolute bottom-0 right-0 p-1 bg-gray-600 hover:bg-gray-500 rounded-xl text-white cursor-pointer font-Shippori">注文</button>
                    </div>
                </div>
            </div>
        </div>


        <div id="order" v-if="isShow.AddCart"
            class="sticky h-screen w-screen bg-gray-500 bg-opacity-75 inset-0 z-50 flex justify-center items-center px-4 sm:px-6 lg:px-8">
            <div class="max-w-md w-full h-2/3 min-h-500px max-h-1000px relative">
                <div
                    class="bg-white max-w-md w-full h-full min-h-500px max-h-1000px rounded-3xl overflow-x-hidden flex flex-col justify-between relative">
                    <div class="h-1/3 w-full overflow-hidden flex justify-center items-center">
                        <img :src="orderItem.imgSrc" alt="">
                    </div>
                    <div class="pl-4 py-2">
                        <h2 class="font-Yuji text-3xl">{{orderItem.name}}</h2>
                    </div>
                    <div class="flex-grow flex-shrink-0 h-0 overflow-x-hidden w-full">
                        <ul>
                            <li>
                                <div class="bg-gray-200 flex justify-between items-center h-12 pl-4">
                                    <p>お粥の量</p>
                                    <button class="pr-8" :class="classObj.btn" @click=handleBtn>
                                        <ChevronDownIcon class="h-8 w-8 p-1 border border-gray-500 bg-white rounded-full" />
                                    </button>
                                </div>
                                <div class="pl-4 py-2">
                                    <div class="selectionList" v-if="this.classObj.btn.selectionOn">
                                        <div class="flex items-center">
                                            <input name="quantity" type="radio" value="普通" id="quantity_zhong"
                                                class="h-4 w-4 text-indigo-600 focus:ring-indigo-500 border-gray-300 rounded" />
                                            <label for="quantity_zhong" class="ml-2 block text-sm text-gray-900">
                                                普通
                                            </label>
                                        </div>
                                        <div class="flex items-center">
                                            <input  name="quantity" type="radio" value="大盛り" id="quantity_da"
                                                class="h-4 w-4 text-indigo-600 focus:ring-indigo-500 border-gray-300 rounded" />
                                            <label for="quantity_da" class="ml-2 block text-sm text-gray-900">
                                                大盛り
                                            </label>
                                        </div>
                                    </div>
                                </div>
                            </li>
                        </ul>
                    </div>
                    <div class="flex justify-center items-center h-12 w-full">
                        <div class="flex justify-center items-center w-8 h-8 border border-gray-500 rounded-full cursor-pointer select-none"
                            @click=countSub> - </div>
                        <div class="flex justify-center items-center mx-4 select-none"> {{itemCount}} </div>
                        <div class="flex justify-center items-center w-8 h-8 border border-gray-500 rounded-full cursor-pointer select-none"
                            @click=countAdd> + </div>
                    </div>
                    <div class="h-12 w-full">
                        <button class="bg-black hover:bg-opacity-80 text-white font-Shippori w-full h-full" @click=cartAdd>カートに追加</button>
                    </div>
                </div>
                <div class="absolute -top-8 right-1">
                    <button type="button"
                        class="rounded-md text-gray-300 hover:text-white focus:outline-none focus:ring-2 focus:ring-white"
                        @click=orderClose>
                        <XIcon class="h-6 w-6 " />
                    </button>
                </div>
            </div>
        </div>
        <Cart />
    </div>
</template>
<script>
    import Nav from "@/components/nav"
    import Cart from "@/components/cart"

    import {
        XIcon,ChevronDownIcon
    } from '@heroicons/vue/outline'

    export default {
        name: "menuPage",

        components: {
            Nav,
            Cart,
            XIcon,
            ChevronDownIcon
        },

        data() {
            return {
                lists: [{
                        id: "001",
                        name: "粥霸王",
                        price: "1280",
                        description: "赤身肉＋烏賊＋蝦仁＋レバー+ピータン+卵。",
                        imgSrc: require('../../assets/item/001.jpeg')
                    },
                    {
                        id: "002",
                        name: "海鮮及第粥",
                        price: "880",
                        description: "蟹＋干し貝柱＋烏賊＋蝦仁+ショウガ+セロリ+卵。",
                        imgSrc: require('../../assets/item/002.jpeg')
                    },
                    {
                        id: "003",
                        name: "吻仔魚粥",
                        price: "880",
                        description: "赤身肉＋しらす＋ハゲイトウ+卵。",
                        imgSrc: require('../../assets/item/003.jpeg')
                    },
                    {
                        id: "004",
                        name: "虱目魚肚粥",
                        price: "880",
                        description: "サバヒー+ショウガ+セロリ",
                        imgSrc: require('../../assets/item/004.jpeg')
                    },
                    {
                        id: "005",
                        name: "香菇鶏肉粥",
                        price: "880",
                        description: "きのこ+鶏肉＋卵。",
                        imgSrc: require('../../assets/item/005.jpeg')
                    }
                ],
                isShow: {
                    AddCart: false,
                },
                orderItem: null,
                itemCount: null,
                //cartList: [],
                classObj: {
                    btn: {
                        selectionOn: true,
                    },
                },
            }
        },

        methods: {
            order(item) {
                if (this.$store.state.cartList.payView) return;
                this.isShow.AddCart = true;
                this.orderItem = item;
                this.itemCount = 1;
                this.stopMove();
            },
            orderClose() {
                this.isShow.AddCart = false;
                this.Move();
            },
            handleBtn() {
                this.classObj.btn.selectionOn = !this.classObj.btn.selectionOn;
            },
            countSub() {
                this.itemCount--;
                if (this.itemCount <= 1) {
                    this.itemCount = 1;
                }
            },
            countAdd() {
                this.itemCount++;
            },
            cartAdd() {
                let item = {
                    item: this.orderItem,
                    count: this.itemCount,
                    total: null,
                };
                item.total = item.item.price * item.count;
                this.cartList.push(item);
                console.log(this.cartList)
                this.isShow.AddCart = false;
                this.Move();
            },
            stopMove() {
                document.body.style.overflow = 'hidden';
            },
            Move() {
                document.body.style.overflow = ''; //出现滚动条
            }
        },

        computed: {
            payView() {
                return this.$store.state.cartList.payView
            },
            cartList() {
                return this.$store.state.cartList.Value
            }
        },

        /* watch: {
            cartList: {
                handler(newValue) {
                    this.$store.commit('cartList/CARTLIST', newValue);
                },
                immediate: true,
                deep: true,
            },
        } */
    }
</script>