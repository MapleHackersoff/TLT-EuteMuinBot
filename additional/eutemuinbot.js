var arkjarawhrkjqhwrkjqhwrkjqhwrkjqhwrkjqhwrkjqhwrjhrjwqhr = require("./config.json");
var Discord = require("discord.js");
var AES = require("crypto-js/aes");
var CryptoJs = require("crypto-js");
var mineflayer = require("mineflayer");
var nodeBase64 = require('nodejs-base64-converter');
var hewakjrchakwjhrcakwjhrcawkjrhcakwjrhcawkjrhcwakjrchawr = new Discord.Client();
var prefix = arkjarawhrkjqhwrkjqhwrkjqhwrkjqhwrkjqhwrkjqhwrjhrjwqhr.bot.prefix;
var prefixlength = prefix.length;
var channel1 = hewakjrchakwjhrcakwjhrcawkjrhcakwjrhcawkjrhcwakjrchawr.channels.cache.find(channel1 => channel1.name === "eutemuin-logs")

var moderators = [`847566693270290522`,
`847539472471687190`,
`746974212358537267`
];

hewakjrchakwjhrcakwjhrcawkjrhcakwjrhcawkjrhcwakjrchawr.on("ready", () => {
	console.log("Loggined in as "+hewakjrchakwjhrcakwjhrcawkjrhcakwjrhcawkjrhcwakjrchawr.user.tag);
	console.log("Bot ID: "+hewakjrchakwjhrcakwjhrcawkjrhcakwjrhcawkjrhcwakjrchawr.user.id);
})

hewakjrchakwjhrcakwjhrcawkjrhcakwjrhcawkjrhcwakjrchawr.on("message", (hkjcsahrcwarwlkarcwawkrawjrkawrkjwarckawjrclkajwrclakwjra) => {
	if(hkjcsahrcwarwlkarcwawkrawjrkawrkjwarckawjrclkajwrclakwjra.author.bot) return;
	var a = hkjcsahrcwarwlkarcwawkrawjrkawrkjwarckawjrclkajwrclakwjra.content.slice(prefixlength);
	var args = a.split(" ");
	var command = args[0];
	// misc
	if(command.startsWith("ping")){
		hkjcsahrcwarwlkarcwawkrawjrkawrkjwarckawjrclkajwrclakwjra.reply("Pong!");
	} else if(command == "eval") {
    	try {
    		var code = a.slice(5)
    		//+fil
    		if(code.includes("fs")) return;
    		if(code.includes("discord.js")) return;
    		if(code.includes("process.")) return;
    		if(code.includes("new WebSocket")) return;
    		//-fil
    		let evaled = eval(code);
	
    		if (typeof evaled !== "string")
    		  evaled = require("util").inspect(evaled);
	
    		hkjcsahrcwarwlkarcwawkrawjrkawrkjwarckawjrclkajwrclakwjra.reply(clean(evaled), {code:"xl"});
    	} catch (err) {
    		hkjcsahrcwarwlkarcwawkrawjrkawrkjwarckawjrclkajwrclakwjra.reply(`\`[INFO] At line: NaN, char: NaN\` \`\`\`xl\n${clean(err)}\n\`\`\``);
    	}
  	} else if(command == "restart") {
  		if(hkjcsahrcwarwlkarcwawkrawjrkawrkjwarckawjrclkajwrclakwjra.author.id.indexOf(moderators)){
  			restart()
  		} else{
  			hkjcsahrcwarwlkarcwawkrawjrkawrkjwarckawjrclkajwrclakwjra.reply("Not enough permissions.")
  		}
  	}
	// encoding-decoding
	if(command.startsWith("encode")){
		if(args[1] == "base64"){
			var toencode = hkjcsahrcwarwlkarcwawkrawjrkawrkjwarckawjrclkajwrclakwjra.content.slice(14);
			console.log(toencode);
			hkjcsahrcwarwlkarcwawkrawjrkawrkjwarckawjrclkajwrclakwjra.reply(nodeBase64.encode(toencode));
		}
	} else if(command.startsWith("decode")){
		if(args[1] == "base64"){
			var todecode = hkjcsahrcwarwlkarcwawkrawjrkawrkjwarckawjrclkajwrclakwjra.content.slice(14);
			console.log(todecode);
			hkjcsahrcwarwlkarcwawkrawjrkawrkjwarckawjrclkajwrclakwjra.reply(nodeBase64.decode(todecode));
		}
	}
	// minecraft botting
	else if(command.startsWith("mcbot")){
		var args = hkjcsahrcwarwlkarcwawkrawjrkawrkjwarckawjrclkajwrclakwjra.content.slice(6).split(" ");
		var host = args[1].toString();
		var port = args[2].toString();
		var version = 1.12;
		var botCount = 10;
		var bots = [];

		for (let i = 0; i < botCount; i++) {
			var username = getRandomInt(1,5000);
			let bot = bots[i] = mineflayer.createBot({
				host: host,
				port: port,
				username: username,
				version: version.toString()
			})
		}
	}
});

hewakjrchakwjhrcakwjhrcawkjrhcakwjrhcawkjrhcwakjrchawr.login(arkjarawhrkjqhwrkjqhwrkjqhwrkjqhwrkjqhwrkjqhwrjhrjwqhr.bot.token);

function getRandomInt(min, max) {
	min = Math.ceil(min);
	max = Math.floor(max);
	return Math.floor(Math.random() * (max - min)) + min;
};
function clean(text) {
  	if(typeof(text) === "string")
    return text.replace(/`/g, "`" + String.fromCharCode(8203)).replace(/@/g, "@" + String.fromCharCode(8203));
  else
      return text;
}
function restart(){
	process.exit()
}
setInterval(restart, 3600000)
