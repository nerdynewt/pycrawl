#!/bin/env python3


def cdn_checker(header):
    """
    detects websites running on WYSIWYG services
    """
    cdn_name = None
    asp = ['X-Powered-By: ASP.NET', "x-aspnet-version"]
    wordpress = ['x-powered-by: WP Engine', 'wp-json', 'X-Cache-Engine: WP-FFPC', 'x-powered-by Wordpress', 'wpvip.com']
    cloudflare = ['server: cloudflare', '__cfuid', 'cf-cache-status', 'cf-request-id']
    drupal = ['X-Generator: Drupal', 'X-Drupal-Cache', ]
    if header.get('cf-cache-status') or header.get('cf-request-id') or header.get('server') == 'cloudflare':
        cdn_name = 'cloudflare'
    elif header.get('server') == 'squarespace':
        cdn_name = 'squarespace'
    elif header.get('x-powered-by') == "wp engine":
        cdn_name = 'wordpress'
    elif header.get('X-Generator') == "Drupal" or header.get('x-drupal-dynamic-cache') or header.get('x-drupal-cache'):
        cdn_name = 'drupal'
    elif header.get('x-aspnet-version'):
        cdn_name = 'aspnet'
    elif header.get('link'):
        if 'wp-json' in header.get('link'):
            cdn_name = 'wordpress'
    if cdn_name:
        return True, "Uses CDN: "+cdn_name
    else:
        return False, "Unknown CDN"

def corporate(text):
    """
    detects corporate landing websites
    """
    newsspeak = ['Our Products', 'Terms of Use', 'Help Center', 'About Us', 'Privacy Policy','Privacy policy', 'Code of Conduct', 'Cookie Policy', 'Privacy Agreement', 'Terms of Agreement', 'Terms &amp; Conditions', 'Terms of Service', 'Terms of service' 'Contact Us', 'Terms of Use and Disclaimer', 'Press Centre', 'PRIVACY POLICY', 'Diversity', 'Terms of use', 'Privacy statement', 'Cookie policy', 'About us', 'Press releases', 'Cookie Settings', 'Contact us']
    for word in newsspeak:
        if '>'+word+'<' in text:
            return True, "Found newsspeak: "+word
    return False, " "

def validate(content, header):
    if cdn_checker(header)[0]:
        return False, "sinners.txt", cdn_checker(header)[1]
    elif corporate(content)[0]:
        return False, "corporates.txt", corporate(content)[1]
    else:
        return True, "", "No offensive text found"


