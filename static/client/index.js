async function main() {
    console.log('Loading pyodide...')
    const pyodide = await window.loadPyodide({
        indexURL: "https://cdn.jsdelivr.net/pyodide/v0.22.1/full/"
    });

    await pyodide.loadPackage('micropip')
    
    console.log('Loading python...')
    const scriptText = await (await fetch('/index.py')).text();
    pyodide.runPythonAsync(scriptText);
}

main();
