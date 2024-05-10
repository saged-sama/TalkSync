import { redirect } from "@sveltejs/kit";

export const POST = async({ request }: {request:any}) => {
    const body = Object.fromEntries(await request.formData());
    const { username } = body;
    throw redirect(303, `/app/${username}`);
}