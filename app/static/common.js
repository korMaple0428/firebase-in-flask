const cards = [
    {
        img_url : 'https://images.unsplash.com/photo-1587500838691-827ed23dc3e3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=934&q=80',
        title : 'test01', 
        desc : 'test desc'
    },
    {
        img_url : 'https://images.unsplash.com/photo-1587497897222-1d4dbf8634d9?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1000&q=80',
        title : 'test02', 
        desc : 'test desc2'
    },
    {
        img_url : 'https://images.unsplash.com/photo-1537015193695-ffcbb0c7a33f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=934&q=80',
        title : 'test03', 
        desc : 'test desc3'
    },
    {
        img_url : 'https://images.unsplash.com/photo-1559056199-b821a1c9878a?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1266&q=80',
        title : 'test04', 
        desc : 'test desc4'
    },
    {
        img_url : 'https://images.unsplash.com/photo-1516205651411-aef33a44f7c2?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1000&q=80',
        title : 'test05', 
        desc : 'test desc5'
    },
    {
        img_url : 'https://images.unsplash.com/photo-1527061011665-3652c757a4d4?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=933&q=80',
        title : 'test06', 
        desc : 'test desc6'
    },
    {
        img_url : 'https://images.unsplash.com/photo-1560790671-b76ca4de55ef?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=974&q=80',
        title : 'test07', 
        desc : 'test desc7'
    },
    {
        img_url : 'https://images.unsplash.com/photo-1523528283115-9bf9b1699245?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=934&q=80',
        title : 'test08', 
        desc : 'test desc8'
    },
    {
        img_url : 'https://images.unsplash.com/photo-1526781100743-007e0dc2b474?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=976&q=80',
        title : 'test09', 
        desc : 'test desc9'
    },
    {
        img_url : 'https://images.unsplash.com/photo-1489537235181-fc05daed5805?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1351&q=80',
        title : 'test10',
        desc : 'test desc10'
    },
    {
        img_url : 'https://images.unsplash.com/photo-1462275646964-a0e3386b89fa?ixlib=rb-1.2.1&auto=format&fit=crop&w=1400&q=80',
        title : 'test11', 
        desc : 'test desc11'
    },
    {
        img_url : 'https://images.unsplash.com/photo-1461559380858-2dd893d0b0d9?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80',
        title : 'test12', 
        desc : 'test desc12'
    },
    {
        img_url : 'https://images.unsplash.com/photo-1462275646964-a0e3386b89fa?ixlib=rb-1.2.1&auto=format&fit=crop&w=1400&q=80',
        title : 'test13', 
        desc : 'test desc13'
    },
    {
        img_url : 'https://images.unsplash.com/photo-1585061849370-eac21e0d88b0?ixlib=rb-1.2.1&auto=format&fit=crop&w=934&q=80',
        title : 'test14', 
        desc : 'test desc14'
    }
];

const gen_card = (id, card) => {
    return  `
        <div id="card-${id}" class="col-12 col-sm-6 col-md-4 col-lg-2 p-1">
            <div class="card" style="border : none;">
                <img class="img-card-top" src="${card.img_url}" style="object-fit:cover; height:200px;"/>
                <div class="card-body p-1">
                    <div class="card-title mb-1">
                        ${card.title}
                    </div>
                    <div class="card-text">
                        ${card.desc}
                    </div>
                </div>
            </div>
        </div>
        `;
}

const gen_cards = (num_of_cards) => {
    let html = "";
    html += `<div class="row p-1">`;
    for ( const idx of Array(num_of_cards).keys() ) {
        html += gen_card(idx, cards[Math.floor(Math.random()*14)])
    }
    html += `</div>`;

    console.log(html);
    return html;
};
