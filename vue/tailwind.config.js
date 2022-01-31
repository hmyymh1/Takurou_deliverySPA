module.exports = {
  purge: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      animation: {
        'stroke': 'stroke 4s 1s forwards',
        'fadeInOut' : 'fadeInOut 10s infinite',
      },
      keyframes: {
        stroke: {
          '0%': {
            'fill': 'rgba(0, 0, 0, 0)',
            'stroke': 'black',
            'stroke-dasharray': '0 50%',
            'stroke-dashoffset': '25%',
          },
          '70%': {
            'fill': 'rgba(0, 0, 0, 0)',
            'stroke': 'black',
            'stroke-dasharray': '50 0%',
            'stroke-dashoffset': '-25%',
          },
          '100%': {
            'fill': 'black',
            'stroke': 'black',
          },
        },
        fadeInOut: {
          '0%':{
            'opacity': 0,
          },
          '20%,80%':{
            'opacity': 100,
          },
          '100%':{
            'opacity': 0,
          }
        },
      },
      width: {
        '250px': '250px',
      },
      minWidth: {
        '250px':'250px',
        '300px':'300px',
      },
      maxWidth: {
        '1/4': '25%',
        '1/2': '50%',
        '3/4': '75%',
        '7/10': '70%',
      },
      fontFamily: {
        Shippori: ['Shippori Mincho'],
        ZhiMangXing: ['Zhi Mang Xing'],
        Yuji: ['Yuji Mai'],
      },
      letterSpacing: {
        onech: '1ch',
      },
      height: {
        '2screen': '200vh',
      },
      maxHeight: {
        '40vh': '40vh',
        '1/2screen': '50vh',
        '70vh': '70vh',
        '1000px': '1000px',
      },
      minHeight: {
        '500px': '500px',
      },
      borderRadius: {
        '2050': '20% 50%',
      },
      transitionProperty: {
        'width': 'width',
      },
      boxShadow: {
        'nav': '0 1px 10px rgba(0, 0, 0, 0.2)',
      },
      inset: {
        '60%': '60%',
      }
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
}