<template lang="">
    <div id="home" class="w-screen h-screen overflow-hidden">
        <header class="sticky top-0 z-40">
            <Nav/>
        </header>
        <main class="relative top-0 left-0 sm:absolute">
            <div id="topBannerBox" class="opacity-50 w-screen h-screen flex items-center overflow-hidden">
                <div class="flex justify-center lg:justify-start items-center transiton-width ease-linear duration-1000 overflow-hidden h-2screen sm:rounded-r-2050" :class="[classObj.in ? 'sm:max-w-3/4' : 'sm:max-w-7/10']">
                    <img :src=imgSrc alt="" class="max-h-screen max-w-none w-auto animate-fadeInOut sm:min-h-screen sm:max-h-none">
                </div>
            </div>
            <div class="block sm:hidden absolute top-1/4 left-1/4">
                <svg width='600' height='200' viewBox="0 0 600 200" class="transform -rotate-6 fill-current text-transparent">
                    <text x="0" y="40%" class="font-MkPOP text-4xl animate-stroke ">幸せな一日は</text>
                    <text x="20%" y="70%" class="font-MkPOP text-4xl animate-stroke">倬朗から!</text>
                </svg>
            </div>
            <div class="hidden sm:block absolute top-1/3 left-1/4 md:left-1/3 lg:left-1/2 xl:left-60%">
                <svg width='600' height='200' viewBox="0 0 600 200" class="transform -rotate-6 fill-current text-transparent">
                    <text x="0" y="40%" class="font-MkPOP text-6xl animate-stroke">幸せな一日は</text>
                    <text x="40%" y="70%" class="font-MkPOP text-6xl animate-stroke">倬朗から!</text>
                </svg>
            </div>
        </main>
        <Cart/>
    </div>
</template>
<script>

import Nav from "@/components/nav"
import Cart from "@/components/cart" 
 
export default {
    name: "home",
    components: {
        Nav,
        Cart,
    },

    data(){
        return {
            imgSrcData:[
                require('../../assets/homePage/top1.jpg'),
                require('../../assets/homePage/top2.jpg'),
                require('../../assets/homePage/top3.jpg'),
            ],
            imgSrc: null,
            timer: null,
            classObj : {
                in:false,
            }
        }
    },
  
    mounted() {
        setTimeout(() => {
            this.classObj.in = true;
        },)
        this.imgChangeEnd();
        this.imgChangeStart();
    },

    activated() {
        this.imgChangeEnd();
        this.imgChangeStart();
    },

    deactivated () {
        this.imgChangeEnd();
    },

    methods: {
        imgChangeStart(){
            let i = 0,_this = this;
            this.imgSrc = this.imgSrcData[i];
            this.timer = setInterval(() => {
                i++;
                _this.imgSrc = _this.imgSrcData[i];
                if(i == _this.imgSrcData.length - 1){
                    i = -1;
                }
            },10000)
        },
        imgChangeEnd(){
            clearInterval(this.timer);
            this.timer = null;
        }
    }
}
</script>
