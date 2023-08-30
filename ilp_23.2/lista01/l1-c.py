regis1, regis2, regis3 = map(int, input().split())
capt1, capt2, capt3 = map(int, input().split())

print(
    " ".join(
        str(a + b) for a, b in zip([regis1, regis2, regis3], [capt1, capt2, capt3])
    )
)
