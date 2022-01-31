<template>
    <div id='login' class="min-h-screen w-screen">
        <header class="sticky top-0 z-40">
            <Nav />
        </header>
        <div class="min-h-full flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8" id='loginBox'>
            <div class="max-w-md w-full space-y-8">
                <div>
                    <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">
                        ログイン
                    </h2>
                </div>
                <form class="mt-8 space-y-6" method="POST" @submit.prevent="post">
                    <input type="hidden" name="remember" value="true" />
                    <div class="rounded-md shadow-sm -space-y-px">
                        <div>
                            <label for="email-address" class="sr-only">Email address</label>
                            <input name="email" type="email" autocomplete="email" requiindigo=""
                                class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-gray-900 focus:border-gray-900 focus:z-10 sm:text-sm"
                                placeholder="メールアドレス" v-model="user.mailaddress" />
                        </div>
                        <div>
                            <label for="password" class="sr-only">Password</label>
                            <input name="password" type="password" autocomplete="current-password"
                                requiindigo=""
                                class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-gray-900 focus:border-gray-900 focus:z-10 sm:text-sm"
                                placeholder="パスワード" v-model="user.password" />
                        </div>
                    </div>

                    <div class="flex items-center">
                        <input id="remember-me" name="remember-me" type="checkbox"
                            class="h-4 w-4 text-indigo-600 focus:ring-indigo-500 border-gray-300 rounded" />
                        <label for="remember-me" class="ml-2 block text-sm text-gray-900">
                            次回から自動でログインする
                        </label>
                    </div>

                    <div>
                        <button type="submit"
                            class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-red-500 hover:bg-red-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500">
                            ログインする
                        </button>
                    </div>
                </form>
                <div class="text-sm text-center" @click="mailPassRouter">
                    <p class="font-medium text-indigo-600 hover:text-indigo-500 cursor-pointer">
                        パスワードを忘れた方はこちら
                    </p>
                </div>
                <div class="relative flex justify-center">
                    <div class="absolute w-full h-px bg-black top-1/2"></div>
                    <p class="z-10 bg-white px-4">または</p>
                </div>
                <div class="text-sm text-center" @click="registerRouter">
                    <p class="font-medium text-indigo-600 hover:text-indigo-500 cursor-pointer">
                        新規登録
                    </p>
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
        PostRequest
    } from "@/apis/read.js"

    export default {
        name: 'login',

        components: {
            Nav,
            Cart,
        },

        data() {
            return {
                user: {
                    mailaddress: "",
                    password: "",
                }
            }
        },

        methods: {
            registerRouter() {
                this.$router.push('/register');
            },
            mailPassRouter() {
                this.$router.push('/mailPass')
            },
            post() {
                const params = {
                    url: '/user_login',
                    key: '',
                    data: this.user,
                };
                PostRequest(params).then(response => {
                    //console.log(response);
                    if (response.data.resCode == 0) {
                        this.$store.commit('userStore/ISLOGINED', true);
                        this.$store.commit('userStore/USERID', this.user.mailaddress);
                        this.$router.push('/mine/' + this.user.mailaddress);
                        for (let i in this.user) {
                            this.user[i] = "";
                        }
                    } else {
                        alert(response.data.message);
                    }
                });
            },
        }
    }
</script>