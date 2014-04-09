function Regex(type, values) {
	var obj = {};
	obj["type"] = type;
	for (var key in values) {
		obj[key] = values[key];
	}
	return obj;
}

function Literal(s) {
	return Regex("Literal", {"s": s});
}

function Concat(r1, r2) {
	return Regex("Concat", {"r1": r1, "r2": r2});
}

function Choice(r1, r2) {
	return Regex("Choice", {"r1": r1, "r2": r2});
}

function Star(r) {
	return Regex("Star", {"r": r});
}

function accept(regex, chars, k) {
	console.log(JSON.stringify(regex) + " |- " + chars);
	switch (regex["type"]) {
		case "Literal":
			 var s = regex["s"];
			 var first = chars.substr(0, s.length);
			 console.log(chars.substr(chars.length - s.length));
			 if (first === s) {
				 return k(chars.substr(s.length));
			 }
			 return false;
		case "Concat":
			 var r1 = regex["r1"];
			 var r2 = regex["r2"];
			 return accept(r1, chars, function (remaining) {
				 return accept(r2, remaining, k);
			 });
		case "Choice":
			 var r1 = regex["r1"];
			 var r2 = regex["r2"];
			 var first = accept(r1, chars, k);
			 if (first) {
				 return first;
			 }
			 return accept(r2, chars, k);
		case "Star":
			 var r = regex["r"];
			 var first = k(chars);
			 if (first) {
				 return first;
			 }
			 return accept(r, chars, function(remaining) {
					 return accept(regex, remaining, k);
				 });
	}
}

function complete (remaining) {
	console.log("Complete? " + remaining);
	return remaining.length === 0;
}

var regex1 = Concat(Star(Literal("ab")), Literal("abc"));

var regex2 = Choice(Star(Literal("ab")), Concat(Literal("a"), Star(Literal("ba"))));

console.log(accept(Literal("abc"), "abc", complete));
console.log(accept(regex1, "abababc", complete));
console.log(accept(regex1, "abababd", complete));
console.log(accept(regex2, "abababa", complete));
