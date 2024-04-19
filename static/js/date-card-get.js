/*
<article class="date-card ">
    <a href="#" class="user-link">username</a>
    <h5 class="place-of-dating-field">
        Ул. пушкина. Дом колотушкина.
    </h5>
    <p class="date-subscription">
        Ебашим турнир по tekken 5 всем отделом кадров.
    </p>                    
    <h6>7 человек.</h6>
    <a class="date-card-action-button btn btn-primary btn-sm " href="#" role="button"> 
        Согласиться
    </a>
    <div class="date-time-container">
        <p>Дата:  19.04.2024    Время:  19:00</p>
        <p>Длительность:    40 минут</p>
    </div>    

    <div class="remove-float"></div>

</article>
*/

/*
{
    user: {
        name,
        link
    }
    place,
    subscription,
    amountOfPeople,
    date,
    time,
    duration
}
*/

function createDateCardFromJson(jsonData) {
    let card = $('<article class="date-card"></article>');
    let user = $(`<a href=${jsonData.user.link} class="user-link">${jsonData.user.name}</a>`)
    let place = $(`<h5 class="place-of-dating-field">${jsonData.place}</h5>`)
    let subscription = $(`<p class="date-subscription">${jsonData.subscription}</p>`)
    let amountOfPeople = $(`<h6>${jsonData.amountOfPeople} человек.</h6>`)
    let button = $( `<a class="date-card-action-button btn btn-primary btn-sm " href="#" role="button"> 
            Согласиться
        </a>`)
    let dateContainer = $(`<div class="date-time-container">
                            <p>Дата:  ${jsonData.date}    Время:  ${jsonData.time}</p>
                            <p>Длительность:    ${jsonData.duration} минут</p>
                           </div>`)
    let removeFloat = $(`<div class="remove-float"></div>`)

    user.appendTo(card);
    place.appendTo(card);
    subscription.appendTo(card);
    amountOfPeople.appendTo(card);
    button.appendTo(card);
    dateContainer.appendTo(card);
    removeFloat.appendTo(card);

    return card
}

async function getJson(request) {
    // На запрос, сервер должен вернуть именно JSON!!!
    let response = await fetch(request)
    return JSON.parse(response)
}

$(document).ready(function () {
    let testObj = {
        user: {
            name: 'korova natasha',
            link: 'https://google.com/'
        },
        place: 'ул. серафимовича.',
        subscription: 'Послушать ахуительные истории про мифичиский с++',
        amountOfPeople: 15,
        date: '19.04.24',
        time: '12:00',
        duration: '1:35'
    },
    viewTest = createDateCardFromJson(testObj)

    $('#card-place').append(viewTest);
});