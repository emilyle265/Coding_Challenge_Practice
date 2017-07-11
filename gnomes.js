let gnomes = [
    {
        'name': 'Annie',
        'species': 'disco',
        'age': 12,
        'location': 'San Francisco'
    },
    {
        'name': 'Vincent',
        'species': 'zen',
        'age': 20,
        'location': 'Paris'
    },
    {
        'name': 'Herbert',
        'species': 'ninja',
        'age': 30,
        'location': 'Honolulu'
    },
    {
        'name': 'Emma',
        'species': 'firefighter',
        'age': 8,
        'location': 'Tokyo'
    }
];

var data = {'name': [], 'species': [], 'age': [], 'location': []}

for(var i=0; i<gnomes.length; i++) {
    for(var j=0; j<gnomes[i].length; j++) {
        data['name'].push(data[gnomes[i][j]]);
        data['species'].push(data[gnomes[i][j]]);
        data['age'].push(data[gnomes[i][j]]);
        data['location'].push(data[gnomes[i][j]]);
    }
}

for(var i=0; i<gnomes.length; i++) {
    for(var j=0; j<gnomes[i].length; j++) {
        data[gnomes[i][j].key].push(gnomes[i][j].value);
    }
}


// let data = {
//     'name': ['Annie', 'Vincent', 'Herbert', 'Emma'],
//     'species': ['disco', 'zen', 'ninja', 'firefighter'],
//     'age': [12, 20, 30, 8],
//     'location': ['San Francisco', 'Paris', 'Honolulu', 'Tokyo']
// }