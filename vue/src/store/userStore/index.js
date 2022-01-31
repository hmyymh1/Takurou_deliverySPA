const state = {
    userID: '',
    isLogined: false,
    userData: {},
};

const mutations = {
    ISLOGINED(state , payload){
        state.isLogined = payload;
    },
    USERID(state , payload){
        state.userID = payload;
    },
    USERDATA(state , payload){
        if(payload.key == 'userAddressList'){
            state.userData.userAddressList = payload.value;
        }
    }
};

const actions = {

};

export default {
    namespaced: true,
    state,
    mutations,
    actions
}

