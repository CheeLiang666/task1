function convertToTime(timeStr){
    if(timeStr.toLowerCase().search("am") != -1){
        var timeOnly = timeStr.split(" ");
        var timeValue = timeOnly[0].split(":");
        var newTime = "";
        if(timeValue[0].length < 2){
            newTime = "0".concat(timeValue[0], ":", timeValue[1]);
        }else{
            if(timeValue[0] === "12"){
                timeValue[0] = "00";
                newTime = timeValue[0].concat(":", timeValue[1]);
            }else{
                newTime = timeOnly[0];
            }
        }
        return newTime;
    }else{
        var timeOnly = timeStr.split(" ");
        var timeValue = timeOnly[0].split(":");
        var newTime = "";
        if(timeValue[0] === "12"){
            newTime = timeValue[0].concat(":", timeValue[1]);
        }else{
            var timeIn24hour = (parseInt(timeValue[0]) + 12).toString();
            newTime = timeIn24hour.concat(":", timeValue[1]);
        }
        return newTime;
    }
}

function setCheckedRadioButton(value){
    if(value === "True"){
        return true;
    }
    else{
        return false;
    }
}

function validatePhoneFormat(phoneValue){
    //var regex = /^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$/;
    var regex = /^[\+]?[(]?[0-9]{2,3}[)]?[-\s]?[0-9]{3,4}[-\s]?[0-9]{4,6}$/;
    if(phoneValue.match(regex) != null){
        return true;
    }else{
        return false;
    }
}

//testing function
