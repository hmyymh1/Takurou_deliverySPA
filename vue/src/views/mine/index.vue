<template lang="">
    <div id="mine" class="min-h-screen w-screen flex flex-col overflow-x-hidden">
        <header class="sticky top-0 z-40">
            <Nav />
        </header>
        <main class="bg-gray-100 mt-20 flex-1">
            <div class="max-w-2xl mx-auto py-16 px-4 sm:py-24 sm:px-6 lg:max-w-7xl lg:px-8">
                <form action="" id="user_detail">
                    <div id="user_icon_box" class="flex justify-between items-center pb-8 border-b-2 border-gray-300">
                        <div id="imgBox" class="w-24 h-24 bg-gray-500 rounded-full mr-8"></div>
                        <div class="flex-1 flex flex-col justify-between sm:flex-row">
                            <div id="userId" class="flex-1 mb-4">{{userID}}</div>
                            <div id="logout" @click="logout"
                                class="cursor-pointer text-indigo-600 hover:text-indigo-500">
                                ログアウト</div>
                        </div>
                    </div>
                    <div id="user_address_box" class="mt-4 sm:mt-8">
                        <p class="text-3xl sm:text-4xl tracking-widest mb-4 sm:mb-8">お届け先</p>
                        <div id="user_address_list" v-for="item in userAddressList" :key=item.addressId class="ml-4 pl-4 my-8 border-l-2 border-gray-400">
                            <p>{{item.fullAddress}}<span class="float-right text-indigo-500 hover:text-indigo-600 cursor-pointer"
                                    @click=addressDelete(item.addressId)>
                                    削除</span></p>
                            <p class="userName">{{item.firstName + item.givenName + " " + item.tel}}</p>
                        </div>
                        <div id="address_add_form" v-if="isShow.address_add_form" class="w-full">
                            <table class="table-auto border-separate px-4" id="address_add_table">
                                <tr class="postCode">
                                    <th class="text-left">郵便番号(半角数字)<span class="text-red-500">＊</span></th>
                                    <td>
                                        <p>
                                            <input type="text" class="h-8 px-2 w-1/2 mr-4" placeholder="例：1440053"
                                                v-model="user.postCode" @input="getAddress">&nbsp;<a
                                                href="https://www.post.japanpost.jp/zipcode/" target="_blank"
                                                class="underline text-gray-400 hover:text-gray-500">郵便番号を検索</a>
                                        </p>
                                        <p class="mt-2">※数字7ケタ ハイフン無し</p>
                                    </td>
                                </tr>
                                <tr class="prefectures">
                                    <th class="text-left">都道府県<span class="text-red-500">＊</span></th>
                                    <td>
                                        <input type="text" readonly="readonly" placeholder="郵便番号入力すると自動的に入力する"
                                            v-model="user.prefecture" class="bg-transparent cursor-auto outline-none h-8 w-full">
                                    </td>
                                </tr>
                                <tr class="municipality">
                                    <th class="text-left">市区町村<span class="text-red-500">＊</span></th>
                                    <td>
                                        <input type="text" readonly="readonly" placeholder="郵便番号入力すると自動的に入力する"
                                            v-model="user.municipality" class="bg-transparent cursor-auto outline-none h-8 w-full">
                                    </td>
                                </tr>
                                <tr class="adress">
                                    <th class="text-left">番地<span class="text-red-500">＊</span></th>
                                    <td>
                                        <p>
                                            <input type="text" placeholder="例：5-19-14" v-model="user.address" class="h-8 px-2 w-1/2 mr-4"> ※全角入力
                                        </p>
                                    </td>
                                </tr>
                                <tr class="building">
                                    <th class="text-left">ビル・マンション名</th>
                                    <td>
                                        <p>
                                            <input type="text" placeholder="例：六本木◯◯ビル 101号室" v-model="user.building" class="h-8 px-2 w-1/2 mr-4">
                                            ※全角入力
                                        </p>
                                    </td>
                                </tr>
                                <tr class="name">
                                    <th class="text-left">名前<span class="text-red-500">＊</span></th>
                                    <td>
                                        <div>
                                            <div>
                                                姓 <input type="text" placeholder="例：山田" v-model="user.firstName" class="h-8 px-2 w-1/2 mr-4">
                                            </div>
                                            <div class="my-2">
                                                名 <input type="text" placeholder="例：花" v-model="user.givenName" class="h-8 px-2 w-1/2 mr-4">
                                            </div>
                                        </div>
                                    </td>
                                </tr>
                                <tr class="telephone">
                                    <th class="text-left">電話番号(半角数字)<span class="text-red-500">＊</span></th>
                                    <td>
                                        <p>
                                            <input type="tel" placeholder="例：07012345678" v-model="user.tel" class="h-8 px-2 w-1/2 mr-4"> ※ハイフン無し
                                        </p>
                                        <p class="mt-2">※配送の際、確認のためご連絡を差し上げる場合があります。</p>
                                    </td>
                                </tr>
                            </table>
                            <div class="w-full flex justify-center mt-4">
                                <button type="button"
                                    class="bg-gray-900 hover:bg-gray-700 mx-4 text-white cursor-pointer rounded-md text-sm px-2 py-1"
                                    @click="addressAdd">追加</button>
                                <button type="button"
                                    class="bg-gray-900 hover:bg-gray-700 mx-4 text-white cursor-pointer rounded-md text-sm px-2 py-1"
                                    @click="addressCancel">キャンセル</button>
                            </div>
                        </div>
                        <div class="flex justify-center mt-4">
                            <button id="address_add_btn" @click="showAddressForm" type="button"
                                v-if="isShow.address_add_btn"
                                class="text-indigo-600 hover:text-indigo-500">+お届け先を追加する</button>
                        </div>
                    </div>
                </form>
            </div>
        </main>
        <Cart />
    </div>
</template>

<script>
    import Nav from "@/components/nav"
    import Cart from "@/components/cart"
    import axios from "axios"
    import {
        PostRequest
    } from "@/apis/read.js"


    export default {
        name: 'login',

        components: {
            Nav,
            Cart
        },

        data() {
            return {
                user: {
                    postCode: "",
                    prefecture: "",
                    municipality: "",
                    address: "",
                    building: "",
                    fullAddress: "",
                    firstName: "",
                    givenName: "",
                    tel: "",
                    addressId: 0,
                },
                userAddressList: [],
                userOrderLists: [],
                isShow: {
                    address_add_form: false,
                    address_add_btn: true,
                },
            }
        },

        computed: {
            userID() {
                return this.$store.state.userStore.userID
            }
        },

        mounted() {
            if (this.$store.state.userStore.isLogined) {
                return
            } else {
                this.$router.push('/login')
            }
        },

        methods: {
            getAddress() { //输入邮编 从zipaddress获取地址
                const reg = /^\d{7}$/;
                if (!reg.test(this.user.postCode)) {
                    this.user.prefecture = "";
                    this.user.municipality = "";
                    return
                }
                const api_url = 'https://api.zipaddress.net/?zipcode=' + this.user.postCode
                axios.get(api_url)
                    .then((response) => {
                        const data = response.data.data
                        //console.log(data)
                        this.user.prefecture = data.pref
                        this.user.municipality = data.address
                    })
                    .catch((error) => {
                        console.log(error)
                    })
            },
            showAddressForm() {
                this.isShow.address_add_form = true;
                this.isShow.address_add_btn = false;
            },
            addressCancel() {
                this.isShow.address_add_form = false;
                this.isShow.address_add_btn = true;
                const _addressId = this.user.addressId;
                for (let i in this.user) {
                    this.user[i] = "";
                }
                this.user.addressId = _addressId;
            },
            addressAdd() {
                if (this.user.prefecture == "" || this.user.address == "" || this.user.firstName == "" || this.user
                    .lastName == "" || this.user.tel == "") {
                    alert("error");
                    return
                }

                this.user.fullAddress = "〒" + this.user.postCode + ' ' + this.user.prefecture + this.user.municipality +
                    this.user.address + ' ' + this.user.building;
                this.user.addressId++;
                let userAddress = {
                    postCode: this.user.postCode,
                    prefecture: this.user.prefecture,
                    municipality: this.user.municipality,
                    address: this.user.address,
                    building: this.user.building,
                    fullAddress: this.user.fullAddress,
                    addressId: this.user.addressId,
                    firstName: this.user.firstName,
                    givenName: this.user.givenName,
                    tel: this.user.tel,
                }
                this.userAddressList.push(userAddress);

                //提交给后端
                const params = {
                    url: '/address_add',
                    key: this.$store.state.userStore.userID,
                    data: this.userAddressList
                };
                PostRequest(params).then(response => {
                    return response
                })

                this.isShow.address_add_form = false;
                this.isShow.address_add_btn = true;
                const _addressId = this.user.addressId;
                for (let i in this.user) {
                    this.user[i] = "";
                }
                this.user.addressId = _addressId;
            },
            addressDelete(addressId) {
                this.userAddressList.splice(this.userAddressList.findIndex(item => item.addressId === addressId), 1);
                //提交给后端
                const params = {
                    url: '/address_add',
                    key: this.$store.state.userStore.userID,
                    data: this.userAddressList
                };
                PostRequest(params).then(response => {
                    console.log(response);
                })
            },
            getUserData() {
                const params = {
                    url: '/get_user_data',
                    key: this.$store.state.userStore.userID,
                    data: '',
                };
                PostRequest(params).then(response => {
                    //console.log(response);
                    this.userAddressList = response.data.data.addressList;
                    if (this.userAddressList) {
                        this.user.addressId = Number(this.userAddressList[this.userAddressList.length - 1]
                            .addressId);
                    } else {
                        this.user.addressId = 0;
                        this.userAddressList = [];
                    }
                })
            },
            logout() {
                this.$store.commit('userStore/ISLOGINED', false);
                this.$store.commit('userStore/USERID', null);
                this.$router.push('/home')
            }
        },

        watch: {
            '$store.state.userStore.isLogined': {
                handler(newValue) {
                    if (newValue) {
                        this.getUserData();
                    }
                },
                immediate: true,
                deep: true,
            },
            userAddressList: {
                handler(newValue) {
                    this.$store.commit('userStore/USERDATA', {
                        key: 'userAddressList',
                        value: newValue,
                    });
                },
                immediate: true,
                deep: true,
            }
        }
    }
</script>