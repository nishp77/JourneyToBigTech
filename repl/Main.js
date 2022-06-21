function isValid(stale, latest, otjson) {

    const obj = JSON.parse(otjson);
    console.log(obj);

}



isValid(
    'Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.',
    'Repl.it uses operational transformations.',
    '[{"op": "skip", "count": 40}, {"op": "delete", "count": 47}]'
);


