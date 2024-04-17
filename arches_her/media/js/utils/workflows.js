define([
    'arches',
    'knockout'
], function(arches, ko) {
    return {
        getProp: (params, key, prop, isString=false) => {
            if (ko.unwrap(params.value) && params.value()[key]) {
                return prop ? params.value()[key][prop] : params.value()[key];
            } else {
                if (isString) {
                    const emptyStrObject = {};
                    emptyStrObject[arches.activeLanguage] = {
                        "value":'',
                        "direction": arches.languages.find(lang => lang.code == arches.activeLanguage).default_direction
                    };
                    return emptyStrObject;
                } else {
                    return null;
                }
            } 
        }
    };
});