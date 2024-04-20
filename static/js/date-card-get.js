/*
<article class="date-card ">
    <a href="#" class="user-link">username</a>
    <h5 class="date-title">
        Ул. пушкина. Дом колотушкина.
    </h5>
    <p class="date-subscription">
        Ебашим турнир по tekken 5 всем отделом кадров.
    </p>               
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

function createDateCardFromJson(jsonData, isAdding) {
    if(jsonData == null)
        return $(`<article class="date-card"><h5 class="date-title">Нет встреч.</h5></article>`)

    let card = $('<article class="date-card"></article>');
    let user = $(`<a href=${jsonData.user.link} class="user-link">${jsonData.user.name}</a>`)
    let title = $(`<h5 class="date-title">${jsonData.title}</h5>`)
    let subscription = $(`<p class="date-subscription">${jsonData.subscription}</p>`)
    let button = $( `<a class="date-card-action-button btn btn-primary btn-sm " href="#" role="button"> 
            ${isAdding ? 'Согласиться' : 'Удалить'}
        </a>`)
    let dateContainer = $(`<div class="date-time-container">
                            <p>Дата:  ${jsonData.date}    Время:  ${jsonData.time}</p>
                            <p>Длительность:    ${jsonData.duration} минут</p>
                           </div>`)
    let removeFloat = $(`<div class="remove-float"></div>`)

    user.appendTo(card);
    title.appendTo(card);
    subscription.appendTo(card);
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
    viewTest = createDateCardFromJson(null, true)

    $('#card-place').append(viewTest);

    $('find-random-meet').on('click', async function() {
        // /get_random_meet

        let response = await fetch('/get_random_meet'),
            json = JSON.parse(await response.json())
            
        viewCard = createDateCardFromJson(json, true)

        $('#card-place').empty();
        $('#card-place').append(viewCard)
    })
});