const bigInt = require("big-integer");
const crypto = require('crypto');

function generatePrimeAsync(bitLength) {
    return new Promise((resolve) => {
        let isPrime = false;
        let p;
        
        // Loop until a prime number with the desired bit length is found
        while (!isPrime) {
            p = bigInt.randBetween(
                bigInt(2).pow(bitLength - 1),
                bigInt(2).pow(bitLength).subtract(1)
            );

            isPrime = p.isProbablePrime();
        }

        const privateKey = bigInt.randBetween(2, p.subtract(2));

        resolve({ p, a: privateKey });
    });
}

function modPow(base, exponent, modulus) {
    if (modulus.equals(1)) return bigInt(0);
    let result = bigInt(1);
    base = base.mod(modulus);

    while (exponent.gt(0)) {
        if (exponent.mod(2).equals(1)) {
            result = result.multiply(base).mod(modulus);
        }

        exponent = exponent.divide(2);
        base = base.square().mod(modulus);
    }

    return result;
}

function messageToDecimal(message) {
    let value = bigInt(0);

    for (let i = 0; i < message.length; i++) {
        const charCode = message.charCodeAt(i);
        let number = bigInt(0);

        if (charCode >= 97 && charCode <= 122) {
            number = bigInt(charCode - 97);
        }

        if (charCode >= 65 && charCode <= 90) {
            number = bigInt(charCode - 65);
        }

        value = value.add(bigInt(26).pow(message.length - i - 1).multiply(number));
    }

    return value;
}

function decimalToMessage(decimalNumber) {
    if (decimalNumber.lt(0)) {
        return "Invalid input, please enter a non-negative integer.";
    }

    let result = "";

    while (decimalNumber.gt(0)) {
        const remainder = decimalNumber.mod(26);
        result = String.fromCharCode(97 + remainder.toJSNumber()) + result;
        decimalNumber = decimalNumber.divide(26);
    }

    return result || "0";
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function elGamal() {
    await sleep(2000);

    console.log("1. Qúa trình thiết lập bộ khoá");

    await sleep(1500);

    console.log("Thiết lập bộ khoá");

    await sleep(1500);

    console.log("Chọn ra số nguyên tố p có độ dài 1024 bit:");

    await sleep(1000);

    const { p, a } = await generatePrimeAsync(1024);

    console.log("Ta có p = " + p.toString());

    await sleep(1500);

    console.log("Chọn ra alpha là một phần tử nguyên thuỷ theo modp, ta có alpha = 2");

    const alpha = bigInt(2);

    await sleep(1500);

    console.log("Chọn một số nguyên dương a bất kỳ nhỏ hơn p:");

    console.log("Ta có a = " + a.toString());

    await sleep(1500);

    console.log("Tính beta");

    const beta = modPow(alpha, a, p);

    console.log("Ta có beta = " + beta.toString());

    await sleep(1500);

    console.log("Như vậy, ta đã thiết lập bộ khoá K gồm khoá công khai K' và khoá bí mật K''");

    await sleep(2000);

    console.log("Trong đó:");

    await sleep(1000);

    console.log("Khoá công khai K' = (p, alpha, beta)");

    await sleep(1500);

    console.log("Khoá bí mật K'' = a");

    await sleep(1500);

    console.log("2. Qúa trình mã hoá bản tin");

    await sleep(1500);

    const message = "chaomunghaimuoinamthanhlaptruongdhcn";

    console.log("Ta có bản tin với nội dung:" + message);

    await sleep(1500);

    const decimalMessage = messageToDecimal(message);

    console.log("Ta tiến hành chọn ngẫu nhiên k thuộc Z_p*");

    await sleep(1000);

    const k = bigInt(29102002);

    console.log("Ta có k = " + k.toString());

    const y1 = modPow(alpha, k, p);

    const y2 = decimalMessage.multiply(modPow(beta, k, p)).mod(p);

    console.log("Ta có bảng mã C = (y1, y2) = (" + y1.toString() + "," + y2.toString() + ")");

    console.log("3. Tiến hành giải mã");

    const decrypt = y2.multiply(modPow(y1, p.minus(a).minus(1), p)).mod(p);

    console.log("Gía trị của d = " + decrypt.toString());

    const decryptedMessage = decimalToMessage(decrypt);

    console.log("Bản tin được giải mã có nội dung như sau:" + decryptedMessage);

    await sleep(1500);

    if (message === decryptedMessage) {
        console.log("Quá trình mã hoá và giải mã tiến hành thành công!");
    } else {
        console.log("Quá trình mã hoá và giải mã thất bại, bản tin ban đầu và bản tin được giải mã không khớp nhau.");
    }
}

async function sign_and_verify() {
    
}

console.log("Tiến hành quá trình mã hoá, giải mã, ký và kiểm thử chữ ký trên hệ mật ElGamal với độ dài khoá 1024 bit");

elGamal();
