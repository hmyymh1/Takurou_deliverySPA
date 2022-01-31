const state = {
    Value: [],
    payView: false,
    isActive: 0,
};

const mutations = {
    CARTLIST(state , payload){
        state.Value = payload;
    },
    PAYVIEW(state, payload){
        state.payView = payload;
    },
    ISACTIVE(state, payload){
        state.isActive = payload;
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