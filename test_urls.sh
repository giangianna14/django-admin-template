#!/bin/bash

# URL Testing Script for Django Admin Template
# Tests all major endpoints to ensure proper functionality

BASE_URL="http://127.0.0.1:8000"
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "🧪 Testing Django Admin Template URLs..."
echo "Base URL: $BASE_URL"
echo "=========================="

test_url() {
    local url=$1
    local expected_status=${2:-200}
    local response=$(curl -s -o /dev/null -w "%{http_code}" "$url")
    
    if [ "$response" = "$expected_status" ]; then
        echo -e "${GREEN}✅ $url - Status: $response${NC}"
    elif [ "$response" = "302" ] && [ "$expected_status" = "200" ]; then
        echo -e "${YELLOW}🔒 $url - Status: $response (Redirect - likely requires auth)${NC}"
    else
        echo -e "${RED}❌ $url - Status: $response (Expected: $expected_status)${NC}"
    fi
}

echo -e "\n📋 Core Pages:"
test_url "$BASE_URL/"
test_url "$BASE_URL/features/"
test_url "$BASE_URL/our-team/"
test_url "$BASE_URL/faqs/"
test_url "$BASE_URL/contact/"

echo -e "\n🔐 Authentication:"
test_url "$BASE_URL/auth/login/"
test_url "$BASE_URL/auth/register/"
test_url "$BASE_URL/auth/forgot-password/"

echo -e "\n📊 Dashboard (Protected):"
test_url "$BASE_URL/dashboard/" 302
test_url "$BASE_URL/dashboard/analytics/" 302
test_url "$BASE_URL/dashboard/crm/" 302
test_url "$BASE_URL/dashboard/finance/" 302

echo -e "\n🛒 E-commerce (Protected):"
test_url "$BASE_URL/ecommerce/products/" 302
test_url "$BASE_URL/ecommerce/categories/" 302
test_url "$BASE_URL/ecommerce/cart/" 302
test_url "$BASE_URL/ecommerce/orders/" 302

echo -e "\n🎨 UI Components (Protected):"
test_url "$BASE_URL/components/buttons/" 302
test_url "$BASE_URL/components/alerts/" 302
test_url "$BASE_URL/components/cards/" 302
test_url "$BASE_URL/components/modals/" 302

echo -e "\n📚 Learning Management (Protected):"
test_url "$BASE_URL/lms/courses/" 302
test_url "$BASE_URL/lms/instructors/" 302
test_url "$BASE_URL/lms/students/" 302

echo -e "\n📅 Events (Protected):"
test_url "$BASE_URL/events/" 302
test_url "$BASE_URL/events/create/" 302
test_url "$BASE_URL/events/calendar/" 302

echo -e "\n💬 Communication (Protected):"
test_url "$BASE_URL/communication/email/" 302
test_url "$BASE_URL/communication/chat/" 302
test_url "$BASE_URL/communication/calendar/" 302

echo -e "\n🏗️ Project Management (Protected):"
test_url "$BASE_URL/projects/" 302
test_url "$BASE_URL/projects/kanban/" 302
test_url "$BASE_URL/projects/create/" 302

echo -e "\n📁 File Management (Protected):"
test_url "$BASE_URL/files/" 302
test_url "$BASE_URL/files/upload/" 302
test_url "$BASE_URL/files/documents/" 302

echo -e "\n🧾 Invoicing (Protected):"
test_url "$BASE_URL/invoicing/" 302
test_url "$BASE_URL/invoicing/create/" 302
test_url "$BASE_URL/invoicing/list/" 302

echo -e "\n🎧 Support (Protected):"
test_url "$BASE_URL/support/" 302
test_url "$BASE_URL/support/tickets/" 302
test_url "$BASE_URL/support/help/" 302

echo -e "\n👥 User Management (Protected):"
test_url "$BASE_URL/users/" 302
test_url "$BASE_URL/users/list/" 302
test_url "$BASE_URL/users/roles/" 302

echo -e "\n🔧 Admin Interface:"
test_url "$BASE_URL/admin/" 302

echo -e "\n=========================="
echo "🎉 URL Testing Complete!"
echo "Note: Status 302 indicates redirect (usually to login for protected pages)"
echo "Note: Status 200 indicates successful page load"
