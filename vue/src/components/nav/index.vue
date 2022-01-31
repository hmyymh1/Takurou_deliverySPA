<template>
  <Disclosure as="nav" class="bg-transparent py-4" :class="[classObj.nav.scrolling ? 'bg-white shadow-nav' : '']"
    v-slot="{ open }" id="nav">
    <div class="max-w-7xl mx-auto px-2 sm:px-6 lg:px-8">
      <div class="relative flex items-center justify-between h-16">
        <div class="absolute inset-y-0 left-0 flex items-center sm:hidden">
          <!-- Mobile menu button-->
          <DisclosureButton
            class="inline-flex items-center justify-center p-2 rounded-md text-gray-400 hover:text-white hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white">
            <span class="sr-only">Open main menu</span>
            <MenuIcon v-if="!open" class="block h-6 w-6" aria-hidden="true" />
            <XIcon v-else class="block h-6 w-6" aria-hidden="true" />
          </DisclosureButton>
        </div>
        <!-- logo & nav -->
        <div class="flex-1 flex items-center justify-center sm:items-stretch sm:justify-start">
          <div class="flex-shrink-0 flex items-center select-none" id="logo">
            <router-link to="/home">
              <p class="font-ZhiMangXing text-3xl">倬朗<span class="font-Shippori text-base ml-2">Takurou</span></p>
              <span class="font-Yuji tracking-onech">朝食専門店</span>
            </router-link>
          </div>
          <div class="hidden sm:block sm:ml-20 sm:my-auto">
            <div class="flex space-x-4">
              <p v-for="item in navigation" :key="item.name" @click=toPage(item.href)
                :class="[$route.path == item.href ? 'bg-gray-900 text-white' : 'text-gray-700 hover:bg-gray-700 hover:text-white', 'px-3 py-2 rounded-md text-sm font-Shippori cursor-pointer']"
                :aria-current="item.current ? 'page' : undefined">{{ item.name }}</p>
            </div>
          </div>
        </div>
        <!-- cart & user -->
        <div class="absolute inset-y-0 right-0 flex items-center pr-2 sm:static sm:inset-auto sm:ml-6 sm:pr-0">
          <div class="relative mr-4 cursor-pointer" @click="cartShowHandle">
            <img src="../../assets/nav/cart.jpg" alt="">
            <div id="cartCount" class="absolute rounded-full h-2/3 w-2/3 top-0 -right-1 select-none">
              <div
                class="absolute bg-red-500 rounded-full w-full h-full flex justify-center items-center text-xs text-white z-10">
                {{cartList.length}}</div>
              <div
                :class="[classObj.cartCount.isChange ? 'animate-ping' : '', 'absolute bg-red-500 rounded-full w-full h-full flex justify-center items-center text-xs text-white']">
              </div>
            </div>
          </div>
          <div>
            <img src="../../assets/nav/account.jpg" alt="" class="cursor-pointer" @click=accountRouter>
          </div>
        </div>
      </div>
    </div>

    <DisclosurePanel class="sm:hidden">
      <div class="px-2 pt-2 pb-3 space-y-1">
        <DisclosureButton v-for="item in navigation" :key="item.name" as="a" @click=toPage(item.href)
          :class="[$route.path == item.href ? 'bg-gray-900 text-white' : 'text-gray-700 hover:bg-gray-700 hover:text-white', 'block px-3 py-2 rounded-md text-base font-Shippori cursor-pointer']"
          :aria-current="item.current ? 'page' : undefined">{{ item.name }}</DisclosureButton>
      </div>
    </DisclosurePanel>
  </Disclosure>
</template>



<script>
  import {
    Disclosure,
    DisclosureButton,
    DisclosurePanel,
  } from '@headlessui/vue'
  import {
    MenuIcon,
    XIcon
  } from '@heroicons/vue/outline'

  export default {
    name: 'Nav',

    components: {
      Disclosure,
      DisclosureButton,
      DisclosurePanel,
      MenuIcon,
      XIcon,
    },

    data() {
      return {
        navigation: [{
            name: 'MENU',
            href: '/menu',
            current: false
          },
          {
            name: 'ABOUT',
            href: '/about',
            current: false
          },
        ],
        cartShow: this.$store.state.cartShow.Value,
        classObj: {
          nav: {
            scrolling: false,
          },
          cartCount: {
            isChange: false,
          }
        },
        cartList: this.$store.state.cartList.Value,
      }
    },

    mounted() {
      var _this = this;
      window.addEventListener("scroll", () => {
        if (document.documentElement.scrollTop != 0) {
          _this.classObj.nav.scrolling = true;
        } else {
          _this.classObj.nav.scrolling = false;
        }
      })
    },

    methods: {
      cartShowHandle() {
        this.cartShow = !this.$store.state.cartShow.Value;
        this.$store.commit('cartShow/CARTSHOW', this.cartShow);
        this.stopMove();
      },
      accountRouter() {
        if (this.$store.state.userStore.isLogined) {
          this.$router.push('/mine/' + this.$store.state.userStore.userID)
        } else {
          this.$router.push('/login')
        }
      },
      toPage(href) {
        if(href == "/about"){
          alert("このページ現在制作中です");
          return
        }
        this.$router.push(href)
      },
      stopMove() {
        document.body.style.overflow = 'hidden';
      },
    },

    watch: {
      '$store.state.cartList.Value': {
        handler(newValue) {
          this.cartList = newValue;
          this.classObj.cartCount.isChange = true;
          let _this = this;
          setTimeout(function () {
            _this.classObj.cartCount.isChange = false;
          }, 500)
        },
        immediate: true,
        deep: true,
      }
    }

  }
</script>