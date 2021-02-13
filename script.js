fetch("https://exceed8.cpsk-club.xyz/", {mode: "no-cors"})
.then(response => response.json())
.then((datas) => {
        datas.forEach((data) => {
            var div_carpark = document.getElementById("carpark");
            var div_card = document.createElement("div");
            var div_card_header = document.createElement("div")
            var div_card_body = document.createElement("div");

            var h5 = document.createElement("h5");
            var p = document.createElement("p");

            div_card.className = "card text-white bg-success mb-3";
            div_card_header.className = "card-header text-center";
            div_card_body.className = "card-body";
            h5.className = "card-title text-center";

            h5.innerHTML = "Available";
            p.innerHTML = "You can park here!";
            

            if (data.status == 0) {
                div_card.className = "card text-white bg-danger mb-3";
                h5.innerHTML = "Parking";
                p.innerHTML = data.time_end_min - data.time_start_min
            }

            div_carpark.appendChild(div_card);
            div_card.appendChild(div_card_head, div_card_body);
            div_card_body.appendChild(h1, p);
        })
    }
);


