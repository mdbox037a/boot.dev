export function calculateApiCost(numReqs: number, tier?: string) {
    let request_cost = 0.10
    if (tier) {
        if (tier === "pro") {
            request_cost = 0.05
        }
        if (tier === "enterprise") {
            request_cost = 0.03
        }
    }
    return request_cost * numReqs
}
