

var img_address = ["/Static/Images/Black-Forest-Cake.webp","/Static/Images/Red-Velvet-Cake.webp","/Static/Images/Cupcakes.webp","/Static/Images/Sponge-Cakes.webp","/Static/Images/Chocolate-Cake.webp","/Static/Images/Strawberry-Shortcake.webp","/Static/Images/White-Cake.webp"];

function black(){
    var msg = "Black forest cake is perhaps one of the most sumptuous desserts on the planet. It’s so delicious, you’ll want to eat it every day. It has layers of fluffy chocolate sponge, whipped cream, and a cherry filling. This cake is infused with cherry liqueur, bringing a richer and deeper flavor. The combination is nothing short of heavenly!";
    document.getElementById("cake-img").src = img_address[0];
    document.getElementById("set-price").innerHTML = "(₹350)";
    document.getElementById("cake-name").innerHTML = "Black Forest Cake";
    document.getElementById("para-cake").innerHTML = msg;
}
 
function red(){
    var msg = "Red velvet cake is a classic. It’s not just a cake – it’s a symbol of love.The deep, rich cocoa flavor and delicate sweetness are dreamy. It’s coated with fluffy cream cheese icing that ties all the flavors together. And the color! That deep, rich red is so satisfying to look at and so much fun to eat. This cake is perfect for any occasion: birthdays, anniversaries, or just because!";
    document.getElementById("cake-img").src = img_address[1];
    document.getElementById("set-price").innerHTML = "(₹450)";
    document.getElementById("cake-name").innerHTML = "Red Velvet Cake";
    document.getElementById("para-cake").innerHTML = msg;
}

function cup(){
    var msg = "Are you planning a party and need to impress your guests? Or maybe you’re just looking for something sweet to eat Whatever the reason, cupcakes never fail to delight! Nothing beats the fluffy cake base topped with decadent frosting. They’re soft, sweet, and delicious. They come in all sorts of flavors, and you can decorate them to match your liking. These handy little treats are a classic that never goes out of style!";
    document.getElementById("cake-img").src = img_address[2];
    document.getElementById("set-price").innerHTML = "(₹300)";
    document.getElementById("cake-name").innerHTML = "Cup Cakes";
    document.getElementById("para-cake").innerHTML = msg;
}

function sponge(){
    var msg = "Who doesn’t love sponge cake? The light, airy texture and sweet, delicate taste make them a favorite for any occasion But have you ever stopped to think about what makes a sponge cake so perfect? The simple mix of eggs, flour, butter, and sugar is the answer. This cake comes out of the oven fluffed up and perfectly browned. It’s typically served with a dusting of sugar or filled with buttercream.";
    document.getElementById("cake-img").src = img_address[3];
    document.getElementById("set-price").innerHTML = "(₹250)";
    document.getElementById("cake-name").innerHTML = "Sponge Cakes";
    document.getElementById("para-cake").innerHTML = msg;
}

function choco(){
    var msg = "When it comes to desserts, you can’t go wrong with chocolate cake It’s a classic, and this dessert never fails to impress! This rich, luscious cake is always the star of any occasion. It packs moist chocolatey goodness layered with even more chocolatey frosting. Whether celebrating a birthday, an anniversary, or the holidays, chocolate cake is a no-brainer choice!";
    document.getElementById("cake-img").src = img_address[4];
    document.getElementById("set-price").innerHTML = "(₹550)";
    document.getElementById("cake-name").innerHTML = "Chocolate Cakes";
    document.getElementById("para-cake").innerHTML = msg;
}

function straw(){
    var msg = "Have you ever eaten a cake that tastes like a cloud of deliciousness? If not, you should try strawberry shortcake. The moist texture of the cake and the sweet, tart flavor of the strawberries combined is downright addicting. This cake will surely take your tastebuds on a journey of pure joy!";
    document.getElementById("cake-img").src = img_address[5];
    document.getElementById("set-price").innerHTML = "(₹500)";
    document.getElementById("cake-name").innerHTML = "Strawberry Cakes";
    document.getElementById("para-cake").innerHTML = msg;
}

function white(){
    var msg = "White cake is a staple in any baker’s repertoire. It’s a simple, classic cake that tastes great with any filling or frosting. Compared to yellow cakes, white cakes are made with only egg whites instead of whole eggs. This results in a lighter texture and milder flavor that feels like biting into a cloud. Most importantly, you can customize this cake depending on the occasion! Just add some fruit and fillings to make it festive and flavorful. Or, if you want to keep things simple, coat it with buttercream frosting and enjoy!";
    document.getElementById("cake-img").src = img_address[6];
    document.getElementById("set-price").innerHTML = "(₹600)";
    document.getElementById("cake-name").innerHTML = "White Cakes";
    document.getElementById("para-cake").innerHTML = msg;
}
