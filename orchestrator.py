from myorchestrator.utilities.drafting import Drafts

draft = Drafts(
    user="mburu",
    otp_type="user-signup",
    email="kamauisaac192@gmail.com",
    duration=5
)

print(draft.otp_verification())


