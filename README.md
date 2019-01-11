Butterfly therapy center miyapur X road
Ananya gacchibowly
SFA attapur

git config --global list
git config --global user.name <windows user id>
git config --global user.email <you email>
git config --global credential.helper manager

http://www.thinkcode.se/blog/2017/06/24/sharing-state-between-steps-in-cucumberjvm-using-spring
https://huddle.eurostarsoftwaretesting.com/wp-content/uploads/2019/01/UKSTAR_2019_eBook_Bas_Dijkstra.pdf
https://www.npmjs.com/package/winston
https://www.npmjs.com/package/properties-reader
https://www.joecolantonio.com
GCS time portal new userid  K86110
const shell = require("shelljs");
var path = require('path');
var filePath = path.join(__dirname, '../../test.sh');
**/*.json
UITest/reports/cucumber-results/json/report
cucumber_report.json

UITest/reports/cucumber-results/json/report
index.html

shiva
Virgin
£2,580.50 30/04/2019
£14,264.53 09/11/2019

suchi
Virgin
£4,265.41 30/04/2019
£5,659.15 09/04/2019

	These amounts are final amount after you shown bills to me.Don’t add previous things into this
22000	previous tenant
48000	present tenant
3000	material
30000	dad
103000	total my amount
	
22000	carpenter
54300	anna balance
3000	muncipality bribe 
1000	electricity
80300	Total
	
22700	balance to me
4331	I am paying in revese




let momHappy = true;

var willGetNewPhone = new Promise(function(res,rej){
  if(momHappy){
    var phone = {
                brand: 'Samsung',
                color: 'black'
            };
   res(phone);
  }
  else
  {
    rej(new Error("no phone"));
  }

});
var showOFf = async function(phone){
return new Promise(function(res,rej){
     res("my phone"+phone.brand);

});
};
console.log("before");
async function askmom(){
await willGetNewPhone
.then(showOFf)
.then(async function(phone){
await console.log(phone);
})
.catch(async function(msg){
await console.log("dfdsfdsfd"+msg);
});
console.log("after");
}

askmom();








/* ES7 */
const isMomHappy = false;

// Promise
const willIGetNewPhone = new Promise(
    (resolve, reject) => {
        if (isMomHappy) {
            const phone = {
                brand: 'Samsung',
                color: 'black'
            };
            resolve(phone);
        } else {
            const reason = new Error('mom is not happy');
            reject(reason);
        }

    }
);

// 2nd promise
async function showOff(phone) {
    return new Promise(
        (resolve, reject) => {
            var message = 'Hey friend, I have a new ' +
                phone.color + ' ' + phone.brand + ' phone';

            resolve(message);
        }
    );
};

// call our promise
async function askMom() {
    try {
        console.log('before asking Mom');

        let phone = await willIGetNewPhone;
        let message = await showOff(phone);

        console.log(message);
        console.log('after asking mom');
    }
    catch (error) {
        console.log(error.message);
    }
}

(async () => {
    await askMom();
})();





////call, apply,bind
var obj={};
var res = function (a,b,c){
console.log(a+b+c);
}
var arr =['a','b','c'];
res.apply(obj,arr);

var res1 = function (a,b,c){
console.log(this+a+b+c);
}
res.call(obj,'a','b','c');

var res2 = function (a,b,c){
console.log(a+b+c);
}
var fr = res2.bind(obj);
fr('a','b','c');
