import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  const signUpPromise = signUpUser(firstName, lastName);
  const uploadPhotoPromise = uploadPhoto(fileName);

  const results = await Promise.allSettled([signUpPromise, uploadPhotoPromise]);

  return results.map((result) => {
    if (result.status === 'fulfilled') {
      return result.value;
    }
    return { status: 'rejected', value: result.reason.message };
  });
}
