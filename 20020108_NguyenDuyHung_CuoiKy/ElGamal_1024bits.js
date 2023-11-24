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

// Hàm tìm phần tử nghịch đảo x trong modulo p
function modInverse(a, p) {
    function extendedEuclidean(a, b) {
        if (b.eq(0)) {
            return { gcd: a, x: bigInt(1), y: bigInt(0) };
        } else {
            const temp = extendedEuclidean(b, a.mod(b));
            const x = temp.y;
            const y = temp.x.minus(a.divide(b).multiply(temp.y));
            return { gcd: temp.gcd, x, y };
        }
    }

    const gcdObj = extendedEuclidean(bigInt(a), bigInt(p));
    const gcd = gcdObj.gcd;

    if (!gcd.eq(1)) {
        console.error(`k và p - 1 không phải là số nguyên tố cùng nhau.`);
        return null;
    } else {
        let inverse = gcdObj.x.mod(p);
        if (inverse.lt(0)) {
            inverse = inverse.plus(p);
        }
        return inverse.toString();
    }
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

async function ElGamal() {
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

    await sleep(2000);

    console.log("3. Tiến hành giải mã");

    await sleep(1500);

    const decrypt = y2.multiply(modPow(y1, p.minus(a).minus(1), p)).mod(p);

    console.log("Gía trị của d = " + decrypt.toString());

    await sleep(1500);

    const decryptedMessage = decimalToMessage(decrypt);

    console.log("Bản tin được giải mã có nội dung như sau:" + decryptedMessage);

    await sleep(1500);

    if (message === decryptedMessage) {
        console.log("Quá trình mã hoá và giải mã tiến hành thành công!");
    } else {
        console.log("Quá trình mã hoá và giải mã thất bại, bản tin ban đầu và bản tin được giải mã không khớp nhau.");
    }

    await sleep(2000);

    console.log("Qúa trình ký và kiểm thử chữ ký trên hệ mật ElGamal");

    await sleep(2000);

    console.log("1. Qúa trình ký");

    var kInverse = null;

    while (kInverse === null) {
        var k1 = bigInt.randBetween(1, p - 1);
        
        var gamma = modPow(alpha,k1,p);

        kInverse = modInverse(k1,p - 1);
    }
    
    kInverse = bigInt(kInverse);

    var delta = (decimalMessage.minus(a.multiply(gamma).mod(p - 1))).multiply(kInverse).mod(p - 1);

    console.log("delta:" + delta.toString());

    while (delta.lt(0)) {
        delta = delta.add(p.subtract(1));
    }

    const signature = {gamma:gamma, delta:delta};

    await sleep(1500);

    console.log("Ta có hàm kỳ gồm bộ hai giá trị (gamma,delta) = " + gamma.toString() + "," + delta.toString() + ")");

    await sleep(2000);

    console.log("2. Tiến hành thực hiện thuật toán kiểm thử chữ ký");

    const verify_left = (modPow(beta,gamma,p)).multiply(modPow(gamma,delta,p)).mod(p);

    const verify_right = modPow(alpha,decimalMessage,p);

    if (verify_left == verify_right) {
        console.log("Xác thực chữ ký thành công!");
    } else {
        console.log("Xác thực chữ ký thất bại!")
    }

}

console.log("Tiến hành quá trình mã hoá, giải mã, ký và kiểm thử chữ ký trên hệ mật ElGamal với độ dài khoá 1024 bit");

ElGamal();

