const state = {
    Value: false,
};

const mutations = {
    CARTSHOW(state , payload){
        state.Value = payload;
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

