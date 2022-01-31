<template lang="">
    <div id='mailPass' class="min-h-screen w-screen">
        <header class="sticky top-0 z-40">
            <Nav />
        </header>
        <div class="min-h-full flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8" id='mailPassBox'>
            <div class="max-w-md w-full space-y-8">
                <div>
                    <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">
                        パスワード再設定
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

                    <div class="flex">
                        <input name="captcha" type="text" requiindigo=""
                            class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-l-md focus:outline-none focus:ring-gray-900 focus:border-gray-900 focus:z-10 sm:text-sm"
                            placeholder="認証コードを入力してください" v-model="user.code" />
                        <button class="bg-gray-400 p-2 text-white rounded-r-md hover:bg-gray-500" type="button" @click="captcha">認証コードを受信<span
                                v-if=isShow.captchaTime>({{captchaTime}}s)</span>
                        </button>
                    </div>

                    <div>
                        <button type="submit"
                            class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-red-500 hover:bg-red-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500">
                            パスワード再設定する
                        </button>
                    </div>
                </form>
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
        name: 'mailPass',

        components: {
            Nav,
            Cart,
        },

        data() {
            return {
                user: {
                    mailaddress: "",
                    password: "",
                    code: "",
                },
                captchaTime: 60,
                isShow: {
                    captchaTime: false,
                }
            }
        },

        methods: {
            post() {
                const params = {
                    url: '/mail_pass',
                    key: '',
                    data: this.user,
                };
                PostRequest(params).then(response => {
                    alert(response.data.message);
                    if (response.data.resCode == 0) {
                        this.$router.push('/login');
                    }
                });
            },
            captcha() {
                const reg = /^[A-Za-z0-9]+([_\.][A-Za-z0-9]+)*@([A-Za-z0-9\-]+\.)+[A-Za-z]{2,6}$/;
                if (!reg.test(this.user.mailaddress)) {
                    alert('メールアドレスを正しく入力してください。');
                    return false;
                } else {
                    if (!this.isShow.captchaTime) {
                        this.isShow.captchaTime = true;
                        this.captchaTime = 60;
                        let timer = setInterval(() => {
                            this.captchaTime--;
                            if (this.captchaTime == 0) {
                                clearInterval(timer);
                                this.isShow.captchaTime = false;
                            }
                        }, 1000);
                        const params = {
                            url: '/mail_code',
                            key: 'mailPass',
                            data: this.user,
                        };
                        PostRequest(params).then(response => {
                            console.log(response);
                        });
                    } else {
                        return false;
                    }
                }
            }
        }
    }
</script>
