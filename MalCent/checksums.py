from MalCent import ssdeep

import hashlib


def md5(data):
    return hashlib.md5(data).hexdigest()


def sha1(data):
    return hashlib.sha1(data).hexdigest()


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def ssdeep_sum(filename):
    return ssdeep.ssdeep(filename)


def checksums(filename):

    data = open(filename, "rb").read()

    sums = {
        "md5":md5(data),
        "sha1":sha1(data),
        "sha256":sha256(data),
        "ssdeep":ssdeep_sum(filename)
    }

    return sums

if __name__ == "__main__":
    pass