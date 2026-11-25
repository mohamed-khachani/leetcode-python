function sleep(millis: number): Promise<void> {
    return new Promise(res => {
        setTimeout(res, millis)
    })
}


/** 
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */
let t = Date.now()
sleep(100).then(() => console.log(Date.now() - t))