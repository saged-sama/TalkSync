export const handle = async({event, resolve}: {event: any, resolve: any}) => {
    const response = await resolve(event);
    return response;
}