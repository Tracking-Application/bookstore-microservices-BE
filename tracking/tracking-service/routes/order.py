from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from database.db import get_session
from sqlalchemy.sql import func
from models.order import Order
from models.product import Product
from models.user import User

from schemas.order import OrderCreate, OrderStatusUpdate
router = APIRouter()


###############################################################################
# ADMIN – GET TOTAL ORDER 
###############################################################################

@router.get("/total_order/{admin_id}",tags=["Order-Tracking-Services"])
async def admin_total_orders(
    admin_id: int,
    db: AsyncSession = Depends(get_session)
):

    # Verify admin
    result = await db.execute(
        select(User).where(User.id == admin_id)
    )
    admin = result.scalar_one_or_none()

    if not admin or admin.role != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")

    result = await db.execute(
        select(func.count(Order.id))
    )

    total = result.scalar()

    return {
        "total_orders": total
    }

###############################################################################
# ADMIN – Total Orders by DELIVERED
###############################################################################

@router.get("/total/delivered", tags=["Order-Tracking-Services"])
async def total_delivered_orders(
    db: AsyncSession = Depends(get_session)
):

    result = await db.execute(
        select(func.count(Order.id))
        .where(Order.status == "Delivered")
    )

    total = result.scalar()

    return {"total_delivered": total}

###############################################################################
# ADMIN – Total Orders by PENDING
###############################################################################

@router.get("/total/pending", tags=["Order-Tracking-Services"])
async def total_pending_orders(
    db: AsyncSession = Depends(get_session)
):

    result = await db.execute(
        select(func.count(Order.id))
        .where(Order.status == "Pending")
    )

    total = result.scalar()

    return {"total_pending": total}

###############################################################################
# ADMIN – Total Orders by SHIPPING
###############################################################################

@router.get("/total/shipping", tags=["Order-Tracking-Services"])
async def total_pending_orders(
    db: AsyncSession = Depends(get_session)
):

    result = await db.execute(
        select(func.count(Order.id))
        .where(Order.status == "Shipping")
    )

    total = result.scalar()

    return {"total_shipping": total}
