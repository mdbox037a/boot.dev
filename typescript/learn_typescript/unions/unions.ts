export function getTicketInfo(id: string | number) {
    if (typeof id === "string") {
        const fields = id.split("-")
        id = parseInt(fields[1], 10)
    }
    return `Processing ticket: ${id}`
}

